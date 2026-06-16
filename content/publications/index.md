---
title: "Publications and Acknowledgements"
description: "Publications and Acknowledgements"
date: 2026-05-08
showTableOfContents: false
showReadingTime: false
---

## Acknowledgements

Papers where I am credited for infrastructure contributions rather than
listed as an author.

### Virchow: A Million-Slide Digital Pathology Foundation Model
**E. Vorontsov, et al.** · arXiv preprint, 2023

A 632M-parameter self-supervised vision transformer for computational
pathology, trained on a million-slide whole-slide image archive from
Memorial Sloan Kettering Cancer Center. Later published in
[*Nature Medicine*](https://www.nature.com/articles/s41591-024-03141-0) (2024).

*Contribution: Built and operated the GPU compute infrastructure and high-throughput storage environment used to train and validate the model.*

[arXiv](https://arxiv.org/abs/2309.07778) ·
[PDF](https://arxiv.org/pdf/2309.07778)

---

### Virchow2: Scaling Self-Supervised Mixed Magnification Models in Pathology
**E. Zimmermann, S. Liu, et al.** · arXiv preprint, 2024

Three vision transformer foundation models trained on 3.1 million
histopathology whole-slide images: Virchow2 (632M), Virchow2G (1.9B),
and Virchow2G Mini (22M distilled). State-of-the-art on 12 tile-level
tasks.

*Contribution: Designed and operated the GPU compute infrastructure and high-throughput storage environment used to train and validate all three models.*

[arXiv](https://arxiv.org/abs/2408.00738) ·
[PDF](https://arxiv.org/pdf/2408.00738)

---

### PRISM: A Multi-Modal Generative Foundation Model for Slide-Level Histopathology
**S. Liu, et al.** · arXiv preprint, 2024

A multi-modal generative foundation model operating at the slide level
for computational pathology, jointly modeling histology and clinical text.

*Contribution: Built and maintained the HPC infrastructure supporting large-scale whole-slide image preprocessing, model training, and validation.*

[arXiv](https://arxiv.org/abs/2405.10254) ·
[PDF](https://arxiv.org/pdf/2405.10254)

---

### PRISM2: Unlocking Multi-Modal General Pathology AI with Clinical Dialogue
**E. Vorontsov, G. Shaikovski, A. Casson, et al.** · arXiv preprint, 2025

A multi-modal slide-level pathology foundation model trained on 700,000
diagnostic specimen-report pairs and 14M question-answer pairs, the
largest vision-and-language histopathology dataset to date. Aligns
histomorphologic features with diagnostic language via clinical-dialogue
supervision.

*Contribution: Built and maintained the HPC infrastructure supporting large-scale whole-slide image preprocessing, model training, and validation.*

[arXiv](https://arxiv.org/abs/2506.13063) ·
[PDF](https://arxiv.org/pdf/2506.13063)

## Co-authored

Papers I co-authored from the Caltech CMS / Large Hadron Collider era.

### SDN-NGenIA: A Software Defined Next Generation Integrated Architecture for HEP and Data Intensive Science
**J. Balcas, et al.** · Journal of Physics: Conference Series, Vol. 898 (CHEP 2016)

A software-defined next-generation integrated architecture supporting
high-energy physics and data-intensive science. Presented at the 22nd
International Conference on Computing in High Energy and Nuclear Physics
(CHEP 2016), San Francisco.

[PDF](/files/sdn-ngenia.pdf)

---

### HTTP as a Data Access Protocol: Trials with XrootD in CMS's AAA Project
**J. Balcas, et al.** · Journal of Physics: Conference Series, Vol. 898 (CHEP 2016)

Evaluation of HTTP as a data access protocol for the CMS Any-data
Anytime Anywhere (AAA) project, comparing performance and operational
characteristics against XrootD's native protocol.

[PDF](/files/httpxrootd.pdf)

---

### High Speed Scientific Data Transfers Using Software Defined Networking
**H. Newman, et al.** · INDIS '15 (SC15), Austin, Texas

Second Workshop on Innovating the Network for Data-Intensive Science,
co-located with SC15: The International Conference for High Performance
Computing, Networking, Storage and Analysis.

[PDF](/files/INDIS2015.pdf)
