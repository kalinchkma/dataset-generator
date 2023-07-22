<!-- @format -->

### Gupta Dynasty Archer-type Coin Datasets:

##### List of kings of the Gupta Dynasty we are working on: (we are working on a specially `archer type` coin)

    * Kumar Gupta 1
    * Skandha Gupta
    * Narashima Gupta
    * Vishnu Gupta
    * Chandra Gupta 2

#### How to add coin details to DataFrame

- Add data to `data.csv`
- Data keys:
  - image_name: string
  - dynasty: string
  - coin_type: string
  - details: string
  - label: string
- Run `python main.py`
  - It will automatically create `data.csv`,`data.xlsx` for us

#### To remove image background we used [U-2-Net] model

[U-2-Net]: https://github.com/xuebinqin/U-2-Net/tree/master
