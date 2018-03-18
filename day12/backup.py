import hashlib
import os
import time
import tarfile
import pickle


def check_md5(fname):
    """检查文件fname的md5值并返回"""
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def md5_to_file(src_dir, md5file):
    """写入md5file, 并返回md5的字典.

    检查源文件夹的所有文件的md5值, 写入文件md5file中,
    并返回一个key为文件全路径, value为md5值的字典"""
    # 所有文件的md5值放入到一个字典中
    md5dict = {}
    # os.walk返回的元素为一个元组, 元组格式为(path, [folders], [files])
    # 可以使用如下方式拆开
    for path, _, files in os.walk(src_dir):
        # files也是一个列表, 需要循环遍历
        for file in files:
            # 得到备份目录的所有文件的全路径
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)
    return md5dict


def full_backup(src_dir, dst_dir, md5file):
    """全量备份.

    备份源文件夹src_dir 中所有文件到目的文件夹dst_dir. 保存为tar.gz文件.
    并把源文件夹中的所有文件的md5计算并保存到md5file中.
    - key为文件全路径
    - value为md5值
    """
    # 备份压缩包的名字, 格式为: <备份目录>_full_<年月日>.tar.gz
    fname = '{}_full_{}.tar.gz'.format(os.path.basename(src_dir.rstrip('/')),
                                       time.strftime('%Y%m%d'))
    # 全路径
    fname = os.path.join(dst_dir, fname)
    # 压缩操作 - 全量备份
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src_dir)
    tar.close()
    # 调用md5_to_file()
    md5dict = md5_to_file(src_dir, md5file)


def incr_bakcup(src_dir, dst_dir, md5file):
    """增量备份.

    新文件, 修改过的文件进行备份.
    通过对比md5值进行判断."""
    fname = '{}_incr_{}.tar.gz'.format(os.path.basename(src_dir.rstrip('/')),
                                       time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)
    # 读入老的md5dict
    with open(md5file, 'rb') as fobj:
        oldmd5 = pickle.load(fobj)
    # 新的md5dict, 新的写入到md5file中
    md5dict = md5_to_file(src_dir, md5file)
    # 增量压缩
    tar = tarfile.open(fname, 'w:gz')
    # 遍历新的字典的key
    for key in md5dict:
        # if key not in oldmd5 or md5dict[key] != oldmd5[key]:
        # key在老的md5dict中不存在, 或key的值和老的不一样, 则进行压缩
        if oldmd5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()


if __name__ == '__main__':
    src_dir = '/tmp/demo/security'
    dst_dir = '/var/tmp/backup'
    md5file = '/var/tmp/backup/md5.data'
    if time.strftime('%a') == 'Mon':
        full_backup(src_dir, dst_dir, md5file)
    else:
        incr_bakcup(src_dir, dst_dir, md5file)
