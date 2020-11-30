# LYNKED_QA_project
repo to host test scripts

## directory structure

### tests
```
<ROOT>
└── tests
    ├── admin                  # test /admin/
    ├── lang
    ├── lib
    ├── manage                 # test /manage/
    ├── self_test
    ├── smoke
    └── UI_test                # test /food/, lineup
```

### reports
hosted in repo QA_test_result
website: https://lynkedkk.github.io/QA_test_result/


## to develop

  - functional test
```
$ pipenv install --dev
```
  - device emulation
    - start a Pixel 4 phone on emulator-5554 (client_device, appium port 4723, 1080x2280)
    - start a Android Tablet device on emulator-5556 (restaurant_device, appium port 5723, 1536x2048)

## progress
  - https://docs.google.com/spreadsheets/d/1pVpmrZH03URWWLjfe9bZxA3nfnf4-qFKSklFdKFEB4o/edit#gid=0

  - ### data sources
  - ### manual test case example shared by danel dada

    - https://docs.google.com/spreadsheets/d/18Wcn9MWp2byJXmWZHl3n03LQLLc1-ykaS3x5ogX8T08/edit?usp=sharing
    - https://drive.google.com/drive/folders/16rzqmaSZPB4Lf90ud5Rtp7kY9haVs_Cb?usp=sharing

### Test network design
![test network/distribution](/docs/test_network.png?raw=true "test network/distribution")


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
