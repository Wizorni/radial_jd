import matplotlib.pyplot as plt
ish = open('PZ_Mon_v_radial_1__1.dat', 'r')
jd = []
vr = []

for line in ish:
    t = line.strip()
    if t == 0:
        del t
    else:
        t = t.lower()
        t = t.split(" ")
        if len(t) != 2:
            del t
        else:
            jd.append(float(t[0]))
            vr.append(float(t[1]))

plt.scatter(jd, vr, color='black', marker='o')
plt.xlabel("MJD 24...")
plt.ylabel('Vr')
plt.title('Measured Vr')
plt.show()