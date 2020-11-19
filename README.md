# QA_test_scripts
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
  - https://drive.google.com/drive/folders/16rzqmaSZPB4Lf90ud5Rtp7kY9haVs_Cb?usp=sharing
