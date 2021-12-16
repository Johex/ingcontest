import unittest
from DocumentProcessor import DocumentProcessor

documentProcessor = DocumentProcessor()

class TestStringMethods(unittest.TestCase):

    documentProcessor = DocumentProcessor()

    def test_0(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/test.png'),'1253748')

    def test_1(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-001.png'), '768029749271')
    def test_2(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-002.png'), '517983182433')
    def test_3(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-003.png'), 'O6435126')
    def test_4(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-004.png'), 'T4818117')
    def test_5(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-005.png'), '646857908629')
    def test_6(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-006.png'), '621878940860')
    def test_7(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-007.png'), '33897845')
    def test_8(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-008.png'), '504813637914')
    def test_9(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-009.png'), '8420858')
    def test_10(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-010.png'), '152561501679')
    def test_11(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-011.png'), '763058297345')
    def test_12(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-012.png'), '537834206386')
    def test_13(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-013.png'), '18107905')
    def test_14(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-014.png'), '499425922575')
    def test_15(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-015.png'), 'Z34233249')
    def test_16(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-016.png'), '768164804774')
    def test_17(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-017.png'), '199208893730')
    def test_18(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-018.png'), 'Z88666047')
    def test_19(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-019.png'), 'L73882131')
    def test_20(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-020.png'), '250146625140')
    def test_21(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-021.png'), '4957646')
    def test_22(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-022.png'), '420873726461')
    def test_23(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-023.png'), '304064436217')
    def test_24(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-024.png'), '609181174143')
    def test_25(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-025.png'), '294047731203')
    def test_26(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-026.png'), '929782896595')
    def test_27(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-027.png'), '676147280501')
    def test_28(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-028.png'), '726368639255')
    def test_29(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-029.png'), '874251934622')
    def test_30(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-030.png'), '583980997597')
    def test_31(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-031.png'), 'L12910589')
    def test_32(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-032.png'), 'Z66992382')
    def test_33(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-033.png'), 'Z44543581')
    def test_34(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-034.png'), '448098226543')
    def test_35(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-035.png'), 'Z85664824')
    def test_36(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-036.png'), '209042746225')
    def test_37(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-037.png'), '334539630779')
    def test_38(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-038.png'), '37145191')
    def test_39(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-039.png'), '569593734063')
    def test_40(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-040.png'), 'A05660987')
    def test_41(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-041.png'), 'N05763263')
    def test_42(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-042.png'), 'R05649728')
    def test_43(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-043.png'), 'D05734030')
    def test_44(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-044.png'), '940222501837')
    def test_45(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-045.png'), 'B05602294')
    def test_46(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-046.png'), 'Z05763689')
    def test_47(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-047.png'), 'R05809749')
    def test_48(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-048.png'), 'K05753162')
    def test_49(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-049.png'), 'W05818842')
    def test_50(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-050.png'), '67331016sys')
    def test_51(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-051.png'), 'T76797461')
    def test_52(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-052.png'), '110077684758')
    def test_53(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-053.png'), 'Z52815290')
    def test_54(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-054.png'), '724695640849')
    def test_55(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-055.png'), '506171782874')
    def test_56(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-056.png'), '159099176947')
    def test_57(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-057.png'), '354728763201')
    def test_58(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-058.png'), '151379373851')
    def test_59(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-059.png'), '39001306')
    def test_60(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-060.png'), 'Z22404242')
    def test_61(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-061.png'), '430970646825')
    def test_62(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-062.png'), 'O39685198')
    def test_63(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-063.png'), '563612053901')
    def test_64(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-064.png'), '811484473519')
    def test_65(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-065.png'), 'L11218472')
    def test_66(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-066.png'), '87793561')
    def test_67(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-067.png'), 'Z73445237')
    def test_68(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-068.png'), 'L19092988')
    def test_69(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-069.png'), '761681803085')
    def test_70(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-070.png'), 'L86086828')
    def test_71(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-071.png'), '630489030472')
    def test_72(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-072.png'), '962377400877')
    def test_73(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-073.png'), 'T11227187')
    def test_74(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-074.png'), '386649783330')
    def test_75(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-075.png'), '69786944')
    def test_76(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-076.png'), '166020326639')
    def test_77(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-077.png'), '324687248656')
    def test_78(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-078.png'), '610126880648')
    def test_79(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-079.png'), 'T76887309')
    def test_80(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-080.png'), 'T54075340')
    def test_81(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-081.png'), '841109288057')
    def test_82(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-082.png'), '634391712695')
    def test_83(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-083.png'), 'L60954374')
    def test_84(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-084.png'), 'T35935475')
    def test_85(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-085.png'), 'L54818373')
    def test_86(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-086.png'), 'L3114612')
    def test_87(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-087.png'), '188651591731')
    def test_88(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-088.png'), '61463028')
    def test_89(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-089.png'), '598680085920')
    def test_90(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-090.png'), 'O15290579')
    def test_91(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-091.png'), '965947846999')
    def test_92(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-092.png'), '308512327321')
    def test_93(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-093.png'), 'L20613861')
    def test_94(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-094.png'), 'Z78203763')
    def test_95(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-095.png'), '29236177')
    def test_96(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-096.png'), 'O53598006')
    def test_97(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-097.png'), '877109715671')
    def test_98(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-098.png'), 'Z31897052')
    def test_99(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-099.png'), '732322560160')
    def test_100(self): self.assertEqual(documentProcessor.retrieveContractNumber('inputfiles/docu-100.png'), '681311731525')


if __name__ == '__main__':
    unittest.main()