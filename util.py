
def seconds_to_h_m_s_ms(seconds: float) -> str:
    int_seconds = int(seconds)
    ms = int(str(seconds).split('.')[1])
    s = int_seconds % 60
    m = int(int(int_seconds / 60) % 60)
    h = int(int_seconds / (60*60))
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:02d}"