def createCheckpoints(sl1,sl2,dl1,dl2):
    midpoints = {}
    mid1 = makeCheckpoints(sl1,sl2,dl1,dl2)
    midpoints['mid1'] = mid1
    mid2 = makeCheckpoints(sl1,sl2,midpoints["mid1"][0],midpoints["mid1"][1])
    midpoints['mid2'] = mid2
    mid3 = makeCheckpoints(midpoints["mid1"][0],midpoints["mid1"][1],dl1,dl2)
    midpoints['mid3'] = mid3
    mid4 = makeCheckpoints(sl1,sl2,midpoints["mid2"][0],midpoints["mid2"][1])
    midpoints['mid4'] = mid4
    mid5 = makeCheckpoints(midpoints["mid2"][0],midpoints["mid2"][1],midpoints["mid1"][0],midpoints["mid1"][1])
    midpoints['mid5'] = mid5
    mid6 = makeCheckpoints(midpoints["mid1"][0],midpoints["mid1"][1],midpoints["mid3"][0],midpoints["mid3"][1])
    midpoints['mid6'] = mid6
    mid7 = makeCheckpoints(midpoints["mid3"][0],midpoints["mid3"][1],dl1,dl2)
    midpoints['mid7'] = mid7
    mid8 = makeCheckpoints(sl1,sl2,midpoints["mid4"][0],midpoints["mid4"][1])
    midpoints['mid8'] = mid8
    mid9 = makeCheckpoints(midpoints["mid4"][0],midpoints["mid4"][1],midpoints["mid2"][0],midpoints["mid2"][1])
    midpoints['mid9'] = mid9
    mid10 = makeCheckpoints(midpoints["mid2"][0],midpoints["mid2"][1],midpoints["mid5"][0],midpoints["mid5"][1])
    midpoints['mid10'] = mid10
    mid11 = makeCheckpoints(midpoints["mid5"][0],midpoints["mid5"][1],midpoints["mid1"][0],midpoints["mid1"][1])
    midpoints['mid11'] = mid11
    mid12 = makeCheckpoints(midpoints["mid1"][0],midpoints["mid1"][1],midpoints["mid6"][0],midpoints["mid6"][1])
    midpoints['mid12'] = mid12
    mid13 = makeCheckpoints(midpoints["mid6"][0],midpoints["mid6"][1],midpoints["mid3"][0],midpoints["mid3"][1])
    midpoints['mid13'] = mid13
    mid14 = makeCheckpoints(midpoints["mid3"][0],midpoints["mid3"][1],midpoints["mid7"][0],midpoints["mid7"][1])
    midpoints['mid14'] = mid14
    mid15 = makeCheckpoints(midpoints["mid7"][0],midpoints["mid7"][1],dl1,dl2)
    midpoints['mid15'] = mid15

    return midpoints

def sortmidpoints(midpoints,source_lat,source_log, destination_lat, destination_log):
    checkpoints = {
           'src' : [source_lat , source_log],
           'checkpoint1' : [midpoints['mid8'][0], midpoints['mid8'][1]],
           'checkpoint2' : [midpoints['mid4'][0], midpoints['mid4'][1]],
           'checkpoint3' : [midpoints['mid9'][0], midpoints['mid9'][1]],
           'checkpoint4' : [midpoints['mid2'][0], midpoints['mid2'][1]],
           'checkpoint5' : [midpoints['mid10'][0], midpoints['mid10'][1]],
           'checkpoint6' : [midpoints['mid5'][0], midpoints['mid5'][1]],
           'checkpoint7' : [midpoints['mid11'][0], midpoints['mid11'][1]],
           'checkpoint8' : [midpoints['mid1'][0], midpoints['mid1'][1]],
           'checkpoint9' : [midpoints['mid12'][0], midpoints['mid12'][1]],
           'checkpoint10' : [midpoints['mid6'][0], midpoints['mid6'][1]],
           'checkpoint11' : [midpoints['mid13'][0], midpoints['mid13'][1]],
           'checkpoint12' : [midpoints['mid3'][0], midpoints['mid3'][1]],
           'checkpoint13' : [midpoints['mid14'][0], midpoints['mid14'][1]],
           'checkpoint14' : [midpoints['mid7'][0], midpoints['mid7'][1]],
           'checkpoint15' : [midpoints['mid15'][0], midpoints['mid15'][1]],
           'dest' : [destination_lat , destination_log]
    }
    return checkpoints

def sort_subCheckpoints(mid_subcheckpoint,d):
    sub_checkpoints = {'sub_checkpoints1': [mid_subcheckpoint['sub_check4'][0],mid_subcheckpoint['sub_check4'][1]],
                        'sub_checkpoints2': [mid_subcheckpoint['sub_check2'][0],mid_subcheckpoint['sub_check2'][1]],
                        'sub_checkpoints3': [mid_subcheckpoint['sub_check5'][0],mid_subcheckpoint['sub_check5'][1]],
                        'sub_checkpoints4': [mid_subcheckpoint['sub_check1'][0], mid_subcheckpoint['sub_check1'][1]],
                        'sub_checkpoints5': [mid_subcheckpoint['sub_check6'][0], mid_subcheckpoint['sub_check6'][1]],
                        'sub_checkpoints6': [mid_subcheckpoint['sub_check3'][0], mid_subcheckpoint['sub_check3'][1]],
                        'sub_checkpoints7': [mid_subcheckpoint['sub_check7'][0], mid_subcheckpoint['sub_check7'][1]],
                        'dest' : [d[0] ,d[1]]
                    }
    return sub_checkpoints

def create_subCheckpoints(s,d):
    mid_subcheckpoint = {}
    sub_check1 = makeCheckpoints(s[0],s[1],d[0],d[1])
    mid_subcheckpoint['sub_check1'] = sub_check1
    sub_check2 = makeCheckpoints(s[0],s[1],sub_check1[0],sub_check1[1])
    mid_subcheckpoint['sub_check2'] = sub_check2
    sub_check3 = makeCheckpoints(sub_check1[0],sub_check1[1],d[0],d[1])
    mid_subcheckpoint['sub_check3'] = sub_check3
    sub_check4 = makeCheckpoints(s[0],s[1],sub_check2[0],sub_check2[1])
    mid_subcheckpoint['sub_check4'] = sub_check4
    sub_check5 = makeCheckpoints(sub_check2[0],sub_check2[1],sub_check1[0],sub_check1[1])
    mid_subcheckpoint['sub_check5'] = sub_check5
    sub_check6 = makeCheckpoints(sub_check1[0],sub_check1[1],sub_check3[0],sub_check3[1])
    mid_subcheckpoint['sub_check6'] = sub_check6
    sub_check7 = makeCheckpoints(sub_check3[0],sub_check3[1],d[0],d[1])
    mid_subcheckpoint['sub_check7'] = sub_check7
    sub_checkpoints = sort_subCheckpoints(mid_subcheckpoint,d)
    return sub_checkpoints


def makeCheckpoints(sl1,sl2,dl1,dl2):
    mid_lat = (sl1 + dl1) / 2
    mid_log = (sl2 + dl2) / 2
    return [mid_lat, mid_log]