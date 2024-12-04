import pandas as pd
from langchain_core.documents import Document


def dataconveter():

    product_data = pd.read_csv('../ecombotdata/flipkart_product_review.csv')
    # print(product_data.columns)
    data = product_data[["product_title", "review"]]


    product_list = []

    for index, row in data.iterrows():

        #construct a object with prod name and the review
        obj = {
            'product_name': row['product_title'],
            'review': row['review']
        }
        product_list.append(obj)



    docs = []
    for entry in product_list:
        metadata = {"product_name": entry['product_name']}
        doc = Document(page_content = entry['review'], metadata=metadata)
        docs.append(doc)

    return docs

#check if the functions works or not
# if __name__ == "__main__":
#     docs = dataconverter()
#     # Print the number of docs created
#     print(f"Number of documents created: {len(docs)}")
#     # Print the first few docs to inspect
#     for doc in docs[:5]:  # Limit to the first 5 documents
#         print(f"Page Content: {doc.page_content}")
#         print(f"Metadata: {doc.metadata}")
#         print("-" * 40)
