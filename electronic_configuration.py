# List of elements with their electronic configurations
elements_config = [
    ("H", "1s1"),
    ("He", "1s2"),
    ("Li", "[He] 2s1"),
    ("Be", "[He] 2s2"),
    ("B", "[He] 2s2 2p1"),
    ("C", "[He] 2s2 2p2"),
    ("N", "[He] 2s2 2p3"),
    ("O", "[He] 2s2 2p4"),
    ("F", "[He] 2s2 2p5"),
    ("Ne", "[He] 2s2 2p6"),
    ("Na", "[Ne] 3s1"),
    ("Mg", "[Ne] 3s2"),
    ("Al", "[Ne] 3s2 3p1"),
    ("Si", "[Ne] 3s2 3p2"),
    ("P", "[Ne] 3s2 3p3"),
    ("S", "[Ne] 3s2 3p4"),
    ("Cl", "[Ne] 3s2 3p5"),
    ("Ar", "[Ne] 3s2 3p6"),
    ("K", "[Ar] 4s1"),
    ("Ca", "[Ar] 4s2"),
    ("Sc", "[Ar] 4s2 3d1"),
    ("Ti", "[Ar] 4s2 3d2"),
    ("V", "[Ar] 4s2 3d3"),
    ("Cr", "[Ar] 4s1 3d5"),
    ("Mn", "[Ar] 4s2 3d5"),
    ("Fe", "[Ar] 4s2 3d6"),
    ("Co", "[Ar] 4s2 3d7"),
    ("Ni", "[Ar] 4s2 3d8"),
    ("Cu", "[Ar] 4s1 3d10"),
    ("Zn", "[Ar] 4s2 3d10"),
    ("Ga", "[Ar] 4s2 3d10 4p1"),
    ("Ge", "[Ar] 4s2 3d10 4p2"),
    ("As", "[Ar] 4s2 3d10 4p3"),
    ("Se", "[Ar] 4s2 3d10 4p4"),
    ("Br", "[Ar] 4s2 3d10 4p5"),
    ("Kr", "[Ar] 4s2 3d10 4p6"),
    ("Rb", "[Kr] 5s1"),
    ("Sr", "[Kr] 5s2"),
    ("Y", "[Kr] 5s2 4d1"),
    ("Zr", "[Kr] 5s2 4d2"),
    ("Nb", "[Kr] 5s2 4d3"),
    ("Mo", "[Kr] 5s1 4d5"),
    ("Tc", "[Kr] 5s2 4d5"),
    ("Ru", "[Kr] 5s2 4d7"),
    ("Rh", "[Kr] 5s2 4d8"),
    ("Pd", "[Kr] 5s2 4d10"),
    ("Ag", "[Kr] 5s1 4d10"),
    ("Cd", "[Kr] 5s2 4d10"),
    ("In", "[Kr] 5s2 4d10 5p1"),
    ("Sn", "[Kr] 5s2 4d10 5p2"),
    ("Sb", "[Kr] 5s2 4d10 5p3"),
    ("I", "[Kr] 5s2 4d10 5p5"),
    ("Xe", "[Kr] 5s2 4d10 5p6"),
    ("Cs", "[Xe] 6s1"),
    ("Ba", "[Xe] 6s2"),
    ("La", "[Xe] 5d1 6s2"),
    ("Ce", "[Xe] 4f1 5d1 6s2"),
    ("Pr", "[Xe] 4f3 6s2"),
    ("Nd", "[Xe] 4f4 6s2"),
    ("Pm", "[Xe] 4f5 6s2"),
    ("Sm", "[Xe] 4f6 6s2"),
    ("Eu", "[Xe] 4f7 6s2"),
    ("Gd", "[Xe] 4f7 5d1 6s2"),
    ("Tb", "[Xe] 4f9 6s2"),
    ("Dy", "[Xe] 4f10 6s2"),
    ("Ho", "[Xe] 4f11 6s2"),
    ("Er", "[Xe] 4f12 6s2"),
    ("Tm", "[Xe] 4f13 6s2"),
    ("Yb", "[Xe] 4f14 6s2"),
    ("Lu", "[Xe] 4f14 5d1 6s2"),
    ("Hf", "[Xe] 4f14 5d2 6s2"),
    ("Ta", "[Xe] 4f14 5d3 6s2"),
    ("W", "[Xe] 4f14 5d4 6s2"),
    ("Re", "[Xe] 4f14 5d5 6s2"),
    ("Os", "[Xe] 4f14 5d6 6s2"),
    ("Ir", "[Xe] 4f14 5d7 6s2"),
    ("Pt", "[Xe] 4f14 5d8 6s2"),
    ("Au", "[Xe] 4f14 5d10 6s1"),
    ("Hg", "[Xe] 4f14 5d10 6s2"),
    ("Tl", "[Xe] 4f14 5d10 6s2 6p1"),
    ("Pb", "[Xe] 4f14 5d10 6s2 6p2"),
    ("Bi", "[Xe] 4f14 5d10 6s2 6p3"),
    ("Po", "[Xe] 4f14 5d10 6s2 6p4"),
    ("At", "[Xe] 4f14 5d10 6s2 6p5"),
    ("Rn", "[Xe] 4f14 5d10 6s2 6p6"),
    ("Fr", "[Rn] 7s1"),
    ("Ra", "[Rn] 7s2"),
    ("Ac", "[Rn] 6d1 7s2"),
    ("Th", "[Rn] 5f1 6d2 7s2"),
    ("Pa", "[Rn] 5f2 6d1 7s2"),
    ("U", "[Rn] 5f3 6d1 7s2"),
    ("Np", "[Rn] 5f4 6d1 7s2"),
    ("Pu", "[Rn] 5f6 6d1 7s2"),
    ("Am", "[Rn] 5f7 6d1 7s2"),
    ("Cm", "[Rn] 5f7 6d2 7s2"),
    ("Bk", "[Rn] 5f9 6d2 7s2"),
    ("Cf", "[Rn] 5f10 6d2 7s2"),
    ("Es", "[Rn] 5f11 6d2 7s2"),
    ("Fm", "[Rn] 5f12 6d2 7s2"),
    ("Md", "[Rn] 5f13 6d2 7s2"),
    ("No", "[Rn] 5f14 6d2 7s2"),
    ("Lr", "[Rn] 5f14 6d3 7s2"),
    ("Rf", "[Rn] 5f14 6d4 7s2"),
    ("Db", "[Rn] 5f14 6d5 7s2"),
    ("Sg", "[Rn] 5f14 6d6 7s2"),
    ("Bh", "[Rn] 5f14 6d7 7s2"),
    ("Hs", "[Rn] 5f14 6d8 7s2"),
    ("Mt", "[Rn] 5f14 6d9 7s2"),
    ("Ds", "[Rn] 5f14 6d10 7s2"),
    ("Rg", "[Rn] 5f14 6d10 7s2 8s1"),
    ("Cn", "[Rn] 5f14 6d10 7s2 8s2"),
    ("Nh", "[Rn] 5f14 6d10 7s2 8s3"),
    ("Fl", "[Rn] 5f14 6d10 7s2 8s4"),
    ("Mc", "[Rn] 5f14 6d10 7s2 8s5"),
    ("Lv", "[Rn] 5f14 6d10 7s2 8s6"),
    ("Ts", "[Rn] 5f14 6d10 7s2 8s7"),
    ("Og", "[Rn] 5f14 6d10 7s2 8s8")
]

def electronic_configuration(a):
    a = input("Enter the symbol of the element: ")
    for i in elements_config:
        if i[0] == a:
            print(i[1])
            break
    else:
        print("Element not found")

electronic_configuration(elements_config)