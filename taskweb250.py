import urllib.request
import collections

def main():
    a = " "
    b = " "
    c = " "
    d = " "
    e = " "
    f = " "
    g = " "
    h = " "
    j = " "
    k = " "
    l = " "
    m = " "
    n = " "
    o = " "
    p = " "
    q = " "
    r = " "
    s = " "
    t = " "
    u = " "
    v = " "
    w = " "
    x = " "
    y = " "
    z = " "
    i = 1
    while i <= 5000:
        resp = urllib.request.urlopen("https://make-some-noise.contest.qctf.ru/6WSjCzum30MOuHJHI25r")
        otvet = str(resp.read())
        a = a + otvet[2]
        b = b + otvet[3]
        c = c + otvet[4]
        d = d + otvet[5]
        e = e + otvet[6]
        f = f + otvet[7]
        g = g + otvet[8]
        h = h + otvet[9]
        j = j + otvet[10]
        k = k + otvet[11]
        l = l + otvet[12]
        m = m + otvet[13]
        n = n + otvet[14]
        o = o + otvet[15]
        p = p + otvet[16]
        q = q + otvet[17]
        r = r + otvet[18]
        s = s + otvet[19]
        t = t + otvet[20]
        u = u + otvet[21]
        v = v + otvet[22]
        w = w + otvet[23]
        x = x + otvet[24]
        y = y + otvet[25]
        z = z + otvet[26]
        i = i + 1
    print(collections.Counter(a).most_common(1))
    print(collections.Counter(b).most_common(1))
    print(collections.Counter(c).most_common(1))
    print(collections.Counter(d).most_common(1))
    print(collections.Counter(e).most_common(1))
    print(collections.Counter(f).most_common(1))
    print(collections.Counter(g).most_common(1))
    print(collections.Counter(h).most_common(1))
    print(collections.Counter(j).most_common(1))
    print(collections.Counter(k).most_common(1))
    print(collections.Counter(l).most_common(1))
    print(collections.Counter(m).most_common(1))
    print(collections.Counter(n).most_common(1))
    print(collections.Counter(o).most_common(1))
    print(collections.Counter(p).most_common(1))
    print(collections.Counter(q).most_common(1))
    print(collections.Counter(r).most_common(1))
    print(collections.Counter(s).most_common(1))
    print(collections.Counter(t).most_common(1))
    print(collections.Counter(u).most_common(1))
    print(collections.Counter(v).most_common(1))
    print(collections.Counter(w).most_common(1))
    print(collections.Counter(x).most_common(1))
    print(collections.Counter(y).most_common(1))
    print(collections.Counter(z).most_common(1))
main()