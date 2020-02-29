import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    lines = wrapper.wrap(string)
    res = ''
    for i in lines:
        res += i + '\n'
    return res

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result