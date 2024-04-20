def get_key_by_value(dct: dict) -> list[int]:
    res = []
    for k, v in dct.items():
        if v is False:
            res.append(k)
    return res
