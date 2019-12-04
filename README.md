# Receipt_Date_Extraction

To use this api use this link:

1.
https://ebefb8f5.ngrok.io/extract_date/ (RECEIPT NAME GIVEN IN RECEIPTS DATASET)

For Example:
https://ebefb8f5.ngrok.io/extract_date/0a0ebd53.jpeg

2. Using Post method:

curl -i -H "Content-Type:application/json" -X POST -d '{"base_64_image_content":"4da45cc9.jpeg"}' https://ebefb8f5.ngrok.io/extract_date

You can use any Image name available in Receipts dataset available.


Dataset Link is here

https://drive.google.com/drive/folders/1tsNzkpVvfbEQDVOFTuverce1CqBUWSYC?usp=sharing

