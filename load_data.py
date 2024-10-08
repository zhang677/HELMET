from data import load_icl
import os

# load_datasets = ["icl_trec_coarse_6600shot_balance",
#                  "icl_trec_fine_6400shot_balance",
load_datasets = ["icl_banking77_5900shot_balance",
                 "icl_clinic150_7050shot_balance",
                 "icl_nlu_8296shot_balance"]

for cur_dataset in load_datasets:
    collection = load_icl(cur_dataset)
    print(collection)
    data = collection["data"]
    keys = data.features.keys()
    os.makedirs(cur_dataset, exist_ok=True)
    for key in keys:
        with open(f"{cur_dataset}/{key}.txt", "w") as f:
            f.write(str(data[0][key]))