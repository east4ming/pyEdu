import shutil

with open('/etc/hosts') as src_fobj:
    with  open('/tmp/zhuji', 'w') as dst_fobj:
        shutil.copyfileobj(src_fobj, dst_fobj)

shutil.copyfile('/etc/hosts', '/tmp/zhuji2')
