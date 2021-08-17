def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):
    
    dd = pol.degree()
    nn = dd * mm + tt

    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)

    # construct lattice B
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    # factor polynomial
    potential_roots = new_pol.roots()
    
    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    return roots

e = 5
N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
C = 23701787746829110396789094907319830305538180376427283226295906585301889543996533410539381779684366880970896279018807100530176651625086988655210858554133345906272561027798171440923147960165094891980452757852685707020289384698322665347609905744582248157246932007978339129630067022987966706955482598869800151693

# RSA known parameters
ZmodN = Zmod(N);

def break_RSA(p_str, max_length_M):
    global e, C, ZmodN

    p_binary_str = ''.join(['{0:08b}'.format(ord(x)) for x in p_str])

    for length_M in range(0, max_length_M+1, 4):          # size of the root

        # Problem to equation (default)
        P.<M> = PolynomialRing(ZmodN) #, implementation='NTL')
        pol = ((int(p_binary_str, 2)<<length_M) + M)^e - C
        dd = pol.degree()

        # Tweak those
        beta = 1                                
        epsilon = beta / 7                      
        mm = ceil(beta**2 / (dd * epsilon))     
        tt = floor(dd * mm * ((1/beta) - 1))    
        XX = ceil(N**((beta**2 / dd) - epsilon))  

        roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)

        if roots:
            return '{0:b}'.format(roots[_sage_const_0 ])

    print('No solution found\n')
    return 0

def bin2char(binary_message):
    if(len(binary_message)%8 != 0):
        binary_message = (8-len(binary_message)%8)*"0" + binary_message
    message = ""
    # print(binary_message)
    for i in range(0,len(binary_message),8):
        # print(binary_message[i:i+8])
        decimal_number = int(binary_message[i:i+8],2)
        # print(decimal_number)
        message += chr(decimal_number)
    return message

if __name__ == "__main__":
    binary_message = break_RSA("You see a Gold-Bug in one corner. It is the key to a treasure found by", 300 )
    if(binary_message):
        print("The root in binary is: " + binary_message)
        print("The password is: " + bin2char(binary_message))