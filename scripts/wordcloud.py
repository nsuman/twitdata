import json
import glob



names = ["AHTBureau", "akhileshU", "ameetdhakal", "Annapurna_Post", "baarakhari", "basantabasnet", "BhagirathYogi", "Bidyabhattarai", "Bijaysspaudel", "brb1954", "ciaa_nepal", "cmprachanda", "doitnepal", "dsmpci", "EONIndia", "eonmoscow", "gbudhathoki", "gsbhusal", "gunaraj", "HelloMoeNepal", "hello_CAANepal", "hello_dotnpl", "Hello_MOALD", "hello_sarkar", "hello_tourismnp", "himalayahd_fre", "himalayahd", "Himal_Khabar", "kantipurdaily", "kathmandupost_freq_dict", "Kishore_Sajha", "Kishore_Sajha_freq_dict", "MilanPandey", "MinendraRijal", "MoCNepal", "MoeapG", "mofaganepal", "MofaNepal", "mofnepal", "MoHAGunaso", "moha_nepal", "ncp_madhavnepal", "nepalembassyUAE", "NepalEmbassyUK", "NepalJudgeNP", "NEPALNPC", "NepalPoliceHQ", "NepalRastraBank", "nepaltourismb", "NepalUNNY", "nepal_of", "nksthaprakash", "Online_khabar", "ParliamentNepal", "PresidentofNP", "PSC_Nepal", "Rajanktm", "ranju_darshana", "Rato_pati", "salokya", "ShahBalen", "Shekharnc", "social_democrac", "speaker_nepal", "sudheerktm", "theanfaofficial", "TheAnnaExpress", "thehimalayan", "thenepalesearmy", "tikaramyatri", "Umesh_Chauhan", "valleytraffic"]

options = []

profiles = json.load(open("../users_profile/users_profile.json"))

for name in names:
    for j in profiles:
        if name == j['username']:
            options.append({
                "label": j['name'],
                "username": name
            })
json.dump(options, open('../word_cloud/names.json', 'w+'))

