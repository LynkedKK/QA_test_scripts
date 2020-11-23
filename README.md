# LYNKED_QA_project
repo to host test scripts

## directory structure

### tests
```
tests
└── UI_test
    ├── functional   # store functional test
    ├── lib          # shared libraries between tests
    ├── new_feature  # store new_feature test
    └── regression   # store regression test
```

### reports
```
reports
├── functional         # store result of functional test
│   ├── assets
│   └── test_viewport
├── new_feature        # store result of new_feature test
│   └── assets
└── regression         # store result of regression test
    └── assets
```

## to develop
```
$ pipenv install --dev
```

## progress
  - https://docs.google.com/spreadsheets/d/1pVpmrZH03URWWLjfe9bZxA3nfnf4-qFKSklFdKFEB4o/edit#gid=0

  - ### data sources
  - ### manual test case example shared by danel dada

    - https://docs.google.com/spreadsheets/d/18Wcn9MWp2byJXmWZHl3n03LQLLc1-ykaS3x5ogX8T08/edit?usp=sharing
    - https://drive.google.com/drive/folders/16rzqmaSZPB4Lf90ud5Rtp7kY9haVs_Cb?usp=sharing

### test sites

  - http://menymeny.com/food/やきとり/?do_lineup

  - http://menymeny.com/manage/やきとり/react
    - new, autorefresh implemented
    - not fully functional
    - Auto refresh at admin lineup page & admin order page

  - http://menymeny.com/manage/やきとり/
    - more mature
    - `passcode: 999999`


### sources
  - https://docs.google.com/presentation/d/1aKvxdUDOCDLrMaJDWzxM0rYl556DdXtsI8vwGKwqRs0/edit#slide=id.g9d43a6522f_0_14
  - https://docs.google.com/spreadsheets/d/191Y9N-LKU1ALCEueEwIey_TnParcaw9ulS9L-m1C71g/edit
  - https://drive.google.com/drive/folders/16rzqmaSZPB4Lf90ud5Rtp7kY9haVs_Cb?usp=sharing
