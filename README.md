# HIVSeqDB

[![](https://img.shields.io/badge/uses-docker-orange)](https://docs.docker.com/get-docker)
[![](https://img.shields.io/badge/uses-conda-yellowgreen)](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
[![](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Twitter Follow](https://img.shields.io/twitter/follow/alfred_ug.svg?style=social)](https://twitter.com/alfred_ug) 

## Introduction

Portable resource for management and analysis of NGS-based HIV Drug Resistance Data.

## Quick installation

+ Download HIVseqDB from GitHub.
    ```bash
    git clone https://github.com/AlfredUg/hivseqdb-docker.git
    cd hivseqdb-docker
    ```

+ Make migrations
    ```bash
    python manage.py makemigrations
    ```

+ Push the migrations
    ```bash
    python manage.py migrate
    ```

+ Create a super user for the admin role
    ```bash
    python manage.py createsuperuser
    ```

## Deploy HIVseqDB using docker-compose

HIVseqDB requires **docker** which is readily available for all operating systems.
```bash
sudo docker-compose up --build -d
```

The server will be running at: http://127.0.0.1. Watch the following video, on how to use the resource.

## Usage

Below is a quick video of the HOW-TOs. 

## Test data

The NGS data used in this demonstration is publically available at the NCBI Sequence Read Archive (SRA) and the European Nucleotide Archive (ENA), Bioproject accession PRJNA340290. Corresponding sample data was obtained from the associated publication. Many thanks to Avila-Ríos, Santiago, et al. "HIV drug resistance in antiretroviral treatment-naïve individuals in the largest public hospital in Nicaragua, 2011-2015." PLoS One 11.10 (2016): e0164156.

```bash
wget /path/to/PRJNA340290/*.fastq.gz 
gunzip *.gz
```

Also here is the corresponding sample metadata.

## Dependancies.

Below is the list of tools that are used by HIVseqDB.

+ [Quasitools](https://phac-nml.github.io/quasitools/)
+ [Sierra-local](https://github.com/PoonLab/sierra-local)

## Troubleshooting

Kindly report any issues at https://github.com/AlfredUg/hivseqdb-docker/issues.

## License

QuasiFlow is licensed under GNU GPL v3.

## Citation

**This work is currently under peer review. A formal citation will be availed in due course.**
