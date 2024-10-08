from data import load_icl

collection = load_icl("icl_trec_coarse_6600shot_balance")
print(collection)
data = collection["data"]
keys = ['text', 'coarse_label', 'fine_label', 'context', 'question', 'answer']
for key in keys:
    with open(f"icl_trec_coarse_6600shot_balance/{key}.txt", "w") as f:
        f.write(str(data[0][key]))