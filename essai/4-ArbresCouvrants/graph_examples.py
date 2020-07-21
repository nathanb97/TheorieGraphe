class Examples:
    """
    Une collection de graphes, pour tests, ...
    """
    def __init__(self, Graph):
        self.Graph = Graph

    def trees(self):
        """
        A collection of trees
        """
        return [self.tree1(), self.G1(), self.Tr1(), self.Tr100()]

    def cyclic(self):
        return [self.G2(), self.G3(), self.G4(),
                self.G10(), self.G20(), self.Gr100(), self.line_cycle()]

    def all(self):
        return [self.C3(), self.T3(), self.cours_1_G(), self.cours_1_reseau(),
                self.directed(), self.undirected(), self.disconnected(),
                self.dijkstra(), self.lines()] + self.trees() + self.cyclic()

    def C3(self):
        return self.Graph((0,1,2), edges=((0,1,1), (1,2,1), (2,0,1)), directed=True)

    def T3(self):
        return self.Graph((0,1,2), edges=((0,1,1), (0,2,1), (1,2,1)), directed=True)

    def cours_1_G(self):
        return self.Graph((0,1,2,3,4,5), edges=((0,2,1), (1,2,1), (2,3,1), (1,5,1), (5,3,1), (3,4,1)))

    def parcours_directed(self):
        A,B,C,D,E,F,G,H = vertices = "A", "B", "C", "D", "E", "F", "G", "H"
        return self.Graph(vertices,
                     edges=((A,B,3), (A,G,2), (A,F,4),
                            (B,C,1), (B,G,1),
                            (C,D,4), (C,G,5), (C,H,2),
                            (D,H,6),
                            (H,F,6),
                            (E,F,3), (E,G,2), (E,H,3),
                            (F,G,1),
                            (G,H,4)), directed=True)

    def cours_1_reseau(self):
        A,B,C,D,E,F,G,H = vertices = list("ABCDEFGH")
        return self.Graph(vertices,
                     edges=((A,B,3), (A,G,2), (A,F,4),
                            (B,C,1), (B,G,1),
                            (C,D,4), (C,G,5), (C,H,2),
                            (D,E,5), (D,H,6),
                            (E,F,3), (E,G,2), (E,H,3),
                            (F,G,1),
                            (G,H,4)), directed=False)

    def dijkstra(self):
        A,B,C,D,E,F,G,H,I,J = vertices = list("ABCDEFGHIJ")
        return self.Graph(vertices=vertices,
                          edges = [ (A,B,87), (A,C,217), (A,E,173),
                                    (B,F,80),
                                    (C,G,186), (C,H,103),
                                    (D,H,183),
                                    (E,J,502),
                                    (F,I,250),
                                    (H,J,167),
                                    (I,J,84) ])

    def directed(self):
        return self.Graph((1,2,3,4), edges=((1,2,12), (1,4,12), (2,3,23)), directed=True)

    def undirected(self):
        return self.Graph((1,2,3,4), edges=((1,2,12), (2,3,23)))

    def disconnected(self):
        return self.Graph((1,2,3,4,5), edges=((1,2,"12"), (2,5,"25"), (3,4, "34")))

    def tree1(self):
        return self.Graph((1,2,3,4,5), edges=((1,3,"12"), (2,3,"23"), (3,4, "34"),
                                              (4,5, "45")))


    def G1(self):
        # pas de Cycle, poids 2.0233065122272356
        return self.Graph([0, 1, 2, 3, 4],
                          edges = [(0, 1, 0.04986897868768314),
                                   (1, 2, 0.8565684439473877),
                                   (0, 3, 0.1873347455017762),
                                   (3, 4, 0.9295343440903883)])

    def G2(self):
        # Cycle [4, 2, 1], poids 0.582873111322098
        return self.Graph([0, 1, 2, 3, 4],
                          edges = [(0, 2, 0.27093387763020926),
                                   (1, 2, 0.9153684407018896),
                                   (1, 3, 0.24725358223169058),
                                   (1, 4, 0.06180530607414725),
                                   (2, 4, 0.18885485178870653),
                                   (3, 4, 0.06127907582903491)])


    # find_cycle(Gsmall) [3, 0, 1], poids 8
    def G3(self):
        return self.Graph((0,1,2,3),
                          edges = [(0,1, 4), (0,2, 8), (0,3, 2),
                                   (1,2, 5), (1,3, 1), (2,3, 7)])

    # find_cycle(G4) [8, 0, 3], poids 3.3008569277636752
    def G4(self):
        return self.Graph([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                          edges = [(0, 2, 0.2893728912897897),
                                   (0, 3, 0.2545143967667245),
                                   (2, 3, 0.9743254563554016),
                                   (0, 4, 0.13613276211990977),
                                   (2, 4, 0.5796020644966668),
                                   (0, 5, 0.14714746059197026),
                                   (0, 6, 0.8862819561171396),
                                   (1, 6, 0.9814314659942929),
                                   (3, 6, 0.6275402970477142),
                                   (5, 6, 0.7519084264450406),
                                   (2, 7, 0.7372652370238395),
                                   (3, 7, 0.20821432300982656),
                                   (0, 8, 0.5888532022624073),
                                   (3, 8, 0.08608459703919125),
                                   (5, 8, 0.6618425167187494),
                                   (7, 8, 0.5573696466722189),
                                   (1, 9, 0.6723814686750504),
                                   (2, 9, 0.879468731223499),
                                   (3, 9, 0.9791617431560409),
                                   (5, 9, 0.9040921416946031)])


    # pas de Cycles, poids 4.307803511233395
    def Tr1(self):
        return self.Graph([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                          edges = [(5, 6, 0.14342321695471938),
                                   (1, 2, 0.14919199336973588),
                                   (7, 8, 0.2932296987312939),
                                   (6, 9, 0.3720125758843773),
                                   (3, 6, 0.44808816879813196),
                                   (4, 9, 0.4636388678365031),
                                   (1, 7, 0.6683028794717232),
                                   (0, 3, 0.8827076911814986),
                                   (5, 8, 0.8872084190054121)])

    
    # find_cycle(G10) [8, 7, 4, 9, 6, 5], poids 3.543715092227983
    def G10(self):
        return self.Graph([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                          edges = [(5, 6, 0.14342321695471938),
                                   (1, 2, 0.14919199336973588),
                                   (7, 8, 0.2932296987312939),
                                   (6, 9, 0.3720125758843773),
                                   (3, 6, 0.44808816879813196),
                                   (4, 9, 0.4636388678365031),
                                   (1, 7, 0.6683028794717232),
                                   (0, 3, 0.8827076911814986),
                                   (5, 8, 0.8872084190054121),
                                   (7, 4, 0.123120000000000)])


    # find_cycle(G20) [19, 0, 4], poids 1.9553007260762039
    def G20(self):
        return self.Graph(range(20),
                          edges = [(0, 3, 0.3634168389615756),
                                   (0, 4, 0.7015260586892916),
                                   (0, 5, 0.7425157651069787),
                                   (0, 6, 0.6526007249929644),
                                   (0, 7, 0.9104398838572075),
                                   (0, 9, 0.31922414154619205),
                                   (0, 10, 0.19623174411481192),
                                   (0, 11, 0.9177995476654177),
                                   (0, 15, 0.4075779897100601),
                                   (0, 16, 0.6267426053660334),
                                   (0, 17, 0.07296441572935863),
                                   (0, 18, 0.4395183918887652),
                                   (0, 19, 0.10720972246443061),
                                   (1, 2, 0.5935194585113542),
                                   (1, 3, 0.8946003974461748),
                                   (1, 7, 0.790995037249055),
                                   (1, 8, 0.5480696351297271),
                                   (1, 11, 0.2793332703105279),
                                   (1, 12, 0.5260978909282017),
                                   (1, 14, 0.004635818801085545),
                                   (1, 15, 0.7583624891938259),
                                   (1, 16, 0.39506432102539846),
                                   (1, 18, 0.19703257352504655),
                                   (1, 19, 0.19352745162500973),
                                   (2, 3, 0.09919733151621013),
                                   (2, 4, 0.36316552644420486),
                                   (2, 5, 0.5276031208968435),
                                   (2, 7, 0.797552121040437),
                                   (2, 9, 0.7260689674869621),
                                   (2, 10, 0.4454843539167215),
                                   (2, 11, 0.45143613319488674),
                                   (2, 13, 0.5882486525001847),
                                   (2, 17, 0.36355248736518453),
                                   (2, 18, 0.5397570823562049),
                                   (3, 4, 0.6446075925217806),
                                   (3, 5, 0.4582685700590986),
                                   (3, 8, 0.1855191117693844),
                                   (3, 12, 0.4170512391987147),
                                   (3, 13, 0.7517745510975751),
                                   (3, 17, 0.4867982530014532),
                                   (4, 5, 0.6931362247154346),
                                   (4, 6, 0.18166675586447634),
                                   (4, 11, 0.6207221174191636),
                                   (4, 12, 0.9412152295799249),
                                   (4, 13, 0.9556851189296002),
                                   (4, 17, 0.7876521777846195),
                                   (4, 18, 0.09846605568334366),
                                   (4, 19, 0.9016699111425092),
                                   (5, 6, 0.817070909004259),
                                   (5, 7, 0.8016220489621028),
                                   (5, 8, 0.6533823005596058),
                                   (5, 9, 0.24603976481898504),
                                   (5, 11, 0.9740595757235172),
                                   (5, 12, 0.8187701654356849),
                                   (5, 14, 0.9376044477200165),
                                   (5, 18, 0.7312781445644063),
                                   (6, 9, 0.03600418635909042),
                                   (6, 13, 0.732998312184104),
                                   (6, 16, 0.44368993755882213),
                                   (6, 17, 0.03596311741821567),
                                   (6, 18, 0.9002143176821802),
                                   (7, 10, 0.013640173297889358),
                                   (7, 11, 0.6309836011200379),
                                   (7, 12, 0.757414879945808),
                                   (7, 14, 0.018352761024553077),
                                   (7, 15, 0.5997213527934385),
                                   (8, 10, 0.8246876114923297),
                                   (8, 11, 0.9763139998790933),
                                   (8, 12, 0.2584403081582627),
                                   (8, 13, 0.9501457843123634),
                                   (8, 16, 0.37050535738038737),
                                   (8, 17, 0.35135679496834626),
                                   (9, 11, 0.8394237512364221),
                                   (9, 12, 0.5315046856309878),
                                   (9, 15, 0.30716277876864184),
                                   (9, 16, 0.29785674365155945),
                                   (9, 19, 0.23217837204429814),
                                   (10, 12, 0.6237703576091194),
                                   (10, 14, 0.4918985368960823),
                                   (10, 16, 0.801202991880257),
                                   (10, 17, 0.5844484375008754),
                                   (10, 19, 0.9289050168095034),
                                   (11, 16, 0.3717001019654633),
                                   (11, 18, 0.5087726632925773),
                                   (11, 19, 0.1878862147994772),
                                   (12, 13, 0.19165987737993373),
                                   (12, 14, 0.3769086092807097),
                                   (12, 16, 0.04733174644850757),
                                   (12, 17, 0.2632760413794065),
                                   (12, 18, 0.27589658231166214),
                                   (12, 19, 0.08751215831184966),
                                   (13, 15, 0.1111217694563158),
                                   (13, 17, 0.01646964884011748),
                                   (13, 18, 0.29028730581005446),
                                   (14, 16, 0.7383270754919118),
                                   (14, 17, 0.7030745972414011),
                                   (14, 18, 0.22235987089899167),
                                   (15, 16, 0.06447398314595643),
                                   (15, 17, 0.14181930938885323),
                                   (17, 19, 0.10847361271600531)])

    def edges100(self):
        return [(26, 60, 0.0009929257344281073),
                (45, 67, 0.0010286724869925656),
                (34, 44, 0.0013846140881925706),
                (0, 58, 0.0016393842333366493),
                (70, 89, 0.0017143616474224466),
                (24, 67, 0.0019890577450794034),
                (6, 82, 0.002249819148925525),
                (31, 80, 0.0028379853089084417),
                (0, 96, 0.0029481304429583854),
                (75, 91, 0.0032638674757965447),
                (9, 10, 0.0037266605507524364),
                (21, 78, 0.0037489087843070035),
                (33, 35, 0.00410834047215225),
                (11, 31, 0.005170707831191335),
                (3, 77, 0.005192052727494234),
                (37, 79, 0.005402800323939472),
                (74, 76, 0.006051125270643887),
                (41, 84, 0.006481236503782739),
                (18, 39, 0.006845605154557788),
                (32, 71, 0.006991120513707205),
                (0, 62, 0.007137610582915066),
                (13, 78, 0.007347510451363615),
                (26, 88, 0.007483924413913767),
                (11, 70, 0.00818023573406057),
                (60, 72, 0.00847593131644242),
                (8, 35, 0.008527184610653826),
                (64, 90, 0.008692626880634657),
                (34, 39, 0.008721229429692112),
                (31, 72, 0.00903700968287735),
                (1, 80, 0.009376682909359113),
                (51, 53, 0.009508227280796921),
                (17, 26, 0.010021539933187107),
                (19, 86, 0.011133733455839234),
                (16, 29, 0.011477878941640096),
                (53, 71, 0.011726501271610568),
                (4, 8, 0.011891758539759767),
                (38, 61, 0.012026827204281165),
                (1, 64, 0.012799943591258023),
                (24, 44, 0.013090669366721874),
                (23, 38, 0.013197218792814214),
                (80, 92, 0.013407517011408965),
                (6, 71, 0.01352040060652171),
                (14, 56, 0.014132658521675001),
                (76, 85, 0.014498149634091018),
                (15, 20, 0.015287879322913422),
                (24, 93, 0.016067918410060722),
                (47, 65, 0.016077539084663695),
                (10, 28, 0.016207361579162027),
                (1, 29, 0.016308730748119782),
                (12, 47, 0.016330538917242343),
                (46, 87, 0.017417180869923943),
                (13, 88, 0.017537396952013395),
                (47, 91, 0.017867673587984356),
                (15, 44, 0.01803494141679285),
                (47, 96, 0.018357856127694916),
                (57, 76, 0.020518204092699444),
                (23, 62, 0.020615407290738963),
                (29, 56, 0.020718523951403833),
                (27, 31, 0.020955156584611112),
                (22, 71, 0.021073273465604947),
                (32, 67, 0.021690243217997063),
                (65, 81, 0.021972605241495913),
                (45, 66, 0.022469342929889446),
                (8, 16, 0.023264661455073776),
                (22, 27, 0.023906230541304474),
                (42, 64, 0.024402796004665994),
                (27, 98, 0.02479261229108376),
                (78, 81, 0.024876769941295285),
                (4, 46, 0.02564741965234174),
                (7, 52, 0.026412579256804625),
                (63, 75, 0.02692683635700166),
                (37, 93, 0.027097227114492695),
                (2, 11, 0.027133305365591776),
                (17, 99, 0.02778769409272952),
                (19, 60, 0.028272132723076382),
                (30, 40, 0.029135399215479696),
                (30, 49, 0.029294783888021536),
                (20, 55, 0.031866641225170245),
                (5, 29, 0.03191260396672879),
                (17, 59, 0.03285247144889514),
                (9, 62, 0.03298716517971134),
                (33, 77, 0.03314073980980381),
                (37, 97, 0.0336793782305469),
                (31, 52, 0.035019335540426244),
                (69, 81, 0.03502865041255365),
                (49, 76, 0.03548798894152094),
                (26, 43, 0.04134901573156036),
                (51, 76, 0.04165437601144362),
                (36, 84, 0.04263525944363655),
                (50, 74, 0.04388051777958912),
                (50, 84, 0.044993159512139114),
                (67, 68, 0.04550434284631266),
                (25, 55, 0.04785288772609797),
                (54, 90, 0.048905722210914604),
                (28, 48, 0.05082878677675229),
                (44, 83, 0.05648970908384521),
                (4, 94, 0.059759500578127955),
                (44, 73, 0.05996282187898894),
                (64, 95, 0.07140214402779765)]

    # Pas de Cycle, Poids 2.010831786660625
    def Tr100(self):
        return self.Graph(range(100), edges = self.edges100())

    # find_cycle(Gr100)
    # [81, 78, 13, 88, 26, 60, 72, 31, 27, 22, 71, 32, 67, 24, 44, 15, 20, 55, 25, 47, 65]
    # poids 2.010831786660625
    def Gr100(self):
        return self.Graph(range(100),
                          edges = self.edges100() +
                          [(76, 41, 0.12312), (25, 47, 0.6435)]
                          )

    def grlines(self, lines):
        """
        >>> Examples(None).grlines([3,1,2])
        [(0, 1, 1), (1, 2, 1), (4, 5, 1)]
        """
        res = []
        cur = 0
        for line in lines:
            for i in range(cur, cur+line-1):
                res.append((i, i+1, 1))
            cur = cur + line
        return res

    def lines(self):
        lns = [3,1,4,2,4,6,1]
        return self.Graph(range(sum(lns)),
                          edges = self.grlines(lns))

    def line_cycle(self):
        lns = [3,1,4,2,4,6,1]
        return self.Graph(range(sum(lns)),
                          edges = self.grlines(lns) + [(12, 10, 1)])
