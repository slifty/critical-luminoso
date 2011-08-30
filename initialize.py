from luminoso.study import StudyDirectory;

claim_dir = "claims"
if not os.path.exists(claim_dir):
    os.makedirs(claim_dir)

StudyDirectory.make_new(claim_dir)