# 2024/3/2 18:28
import random


def get_ua():
    one = random.randint(55, 62)
    two = random.randint(0, 3200)
    thr = random.randint(0, 142)

    os_type = [
        '(Macintosh;U;IntelMacOSX10_6_8;en-us)',
        '(Windows;U;WindowsNT6.1;en-us)',
        '(Windows;U;WindowsNT10.0;en-us)',
        '(Macintosh;IntelMacOSX10.6;rv:2.0.1)',
        '(iPhone;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)',
        '(iPad;U;CPUOS4_3_3likeMacOSX;en-us)'
        '(Macintosh;U;IntelMacOSX10_6_8;en-us)'
    ]
    browser_version = [
        'Chrome/{}.0.{}.{}'.format(one, two, thr),
        'Firefox/{}.0.{}.{}'.format(one, two, thr),
    ]
    ua = [
        f'Mozilla/{random.randint(4, 5)}.0',
        random.choice(os_type),
        f'AppleWebKit/{random.randint(520, 550)}.{random.randint(50, 60)}(KHTML,likeGecko)',
        random.choice(browser_version),
        f'Safari/{random.randint(520, 550)}.{random.randint(10, 20)}'
    ]
    return ''.join(ua)


if __name__ == '__main__':
    print(get_ua())
