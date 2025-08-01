import itertools

def transpose(lines):
    after = itertools.zip_longest(*lines.splitlines(), fillvalue='$')
    return '\n'.join(''.join(word).rstrip('$').replace('$', ' ') for word in after)
    