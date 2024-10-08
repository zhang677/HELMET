from data import load_icl, load_narrativeqa, load_multi_lexsum
import os

load_datasets = ["icl_trec_coarse_6600shot_balance",
                 "icl_trec_fine_6400shot_balance",
                 "icl_banking77_5900shot_balance",
                 "icl_clinic150_7050shot_balance",
                 "icl_nlu_8296shot_balance",
                 "narrativeqa_130772",
                 "multi_lexsum_130372"]

for cur_dataset in load_datasets:
    if not os.path.exists(cur_dataset):
        os.makedirs(cur_dataset, exist_ok=True)
    else:
        print(f"Directory {cur_dataset} already exists. Skipping.")
        continue
    if "icl" in cur_dataset:
        collection = load_icl(cur_dataset)
    elif "narrativeqa" in cur_dataset:
        collection = load_narrativeqa(cur_dataset)
    elif "multi_lexsum" in cur_dataset:
        collection = load_multi_lexsum(cur_dataset)
        os.makedirs(f"{cur_dataset}/summary", exist_ok=True)
    else:
        print(f"Dataset {cur_dataset} not recognized. Skipping.")
        continue
    print(collection)
    data = collection["data"]
    keys = data.features.keys()
    for key in keys:
        with open(f"{cur_dataset}/{key}.txt", "w") as f:
            f.write(str(data[0][key]))