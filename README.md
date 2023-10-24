<!-- @format -->

## Ancient Coinage Datasets:

#### How to add coin details to DataFrame

- Add data:
  - To add data you have to go inside `data` directory there you can add data as
    a `json` file
  - Data keys are:
    - image_name: string
    - dynasty: string
    - coin_type: string
    - details: string
    - label: string
- Run function from `createDataFrame` `main.py`
  - It will automatically create `data.csv`,`data.xlsx` for us
  - It will return `data`, `label`, available `dynasty`, available `coin_type`

#### To remove image background we used [U-2-Net] model

- Image size is `800x800`

[U-2-Net]: https://github.com/xuebinqin/U-2-Net/tree/master
