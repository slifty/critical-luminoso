import json
import urllib

# Update Luminoso study to contain the latest claims and their associated text
study_documents_location = "claims/Documents"
claims_api = "http://127.0.0.1/critical/api/claims/"
corpus_items_api = "http://127.0.0.1/critical/api/corpus_items/"
snippets_api = "http://127.0.0.1/critical/api/snippets/"

# Build up a Luminoso Claim / Corpus Array
# The combined corpus are:
#  - Claim content
#  - Corpus item content associated with the claim
#  - Snippet context associated with the claim

luminoso_claims = dict()

claims_api_response = json.load(urllib.urlopen(claims_api))
for claim in claims_api_response["claims"]:
	# Create an entry for this claim
	luminoso_claims[str(claim["id"])] = []
	
	# Add the claim content
	luminoso_claims[str(claim["id"])].append(claim["content"])
	
	# Add associated corpus item content
	corpus_item_api_response = json.load(urllib.urlopen(corpus_items_api + "?claim_id=" + str(claim["id"])))
	for corpus_item in corpus_item_api_response["corpus_items"]:
		luminoso_claims[str(claim["id"])].append(corpus_item["content"])
	
	
	# Add associated snippet context
	snippet_api_response = json.load(urllib.urlopen(snippets_api + "?claim_id=" + str(claim["id"])))
	print snippets_api + "?claim_id=" + str(claim["id"])
	for snippet in snippet_api_response["snippets"]:
		luminoso_claims[str(claim["id"])].append(snippet["context"])
		
		
# Write the study files -- one per claim ID
for claim_id in luminoso_claims:
	corpus_items = luminoso_claims[claim_id]
	file_name = str(claim_id) + ".txt"
	file_path = study_location + file_name
	FILE = open(file_path,'w')
	for corpus_item in corpus_items:
		FILE.write(corpus_item.encode('UTF-8'))
		FILE.write("\n\n")
	FILE.close()