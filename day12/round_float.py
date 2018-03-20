class RoundFloat(float):
    """从标准类型float进行派生"""
    def __new__(cls, val):
        super(RoundFloat, cls).__new__(cls, round(val, 2))
