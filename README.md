# KAP-PDF

This package downloads pdf attachments from announcements  about Turkish companies from website : https://www.kap.org.tr/en/


## Install

    python setup.py install


## Usage

```bash
# Download all pdf announcments for today:
$  start_download_kap

# Download all pdf announcments from specific date to today:
$  start_download_kap --start_date 2017-03-02

# Download all pdf announcments from specific date  to specific date:
$  start_download_kap --start_date 2016-01-02 --end_date 2017-02-04


# Download all pdf announcments from specific date  to specific date and specify path to Downloads directory :
$  start_download_kap --start_date 2017-03-02 --end_date 2017-03-04 --download_directory ./MyPDFAnnouncments

```
