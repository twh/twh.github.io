---
title: "CV"
description: "CV of Wayne Hendricks, HPC engineer. GPU training infrastructure for foundation models at Paige.AI and Tempus, the DGX-1 cluster at Memorial Sloan Kettering, and the Caltech CMS Tier-2 for the Large Hadron Collider."
date: 2026-05-08
showTableOfContents: true
---

# Thomas Wayne Hendricks

[GitHub](https://github.com/twh) ·
[Google Scholar](https://scholar.google.com/citations?hl=en&user=R2H2QjwAAAAJ) ·
[ORCID](https://orcid.org/0000-0001-9111-8968) ·
[twh@waynehendricks.com](mailto:twh@waynehendricks.com) ·
[Download PDF](/downloads/)

---

## Summary

Paige.AI's founding HPC engineer, from 2018 through its $81M acquisition by Tempus. I built the training infrastructure behind Virchow ([*Nature Medicine*](https://www.nature.com/articles/s41591-024-03141-0), 2024), PRISM, and the company's FDA-cleared diagnostic products, scaling it from 5 to 40+ ML researchers. Before that, HPC at Memorial Sloan Kettering and Caltech.

---

## Career History

### Senior HPC Engineer
**Tempus AI (formerly Paige.AI), New York City**
*2018–Present*

- **Founding HPC engineer at Paige.AI, from 2018 through the September 2025 Tempus acquisition.** Owned end-to-end GPU, storage, scheduling, and multi-cloud infrastructure for clinical foundation model training.
- Built the training infrastructure behind the [Virchow](https://arxiv.org/abs/2309.07778), [Virchow2](https://arxiv.org/abs/2408.00738), [PRISM](https://arxiv.org/abs/2405.10254), and [PRISM2](https://arxiv.org/abs/2506.13063) pathology foundation models and the [OmniScreen](https://arxiv.org/abs/2408.09554) biomarker screening system.
- Architected "Azul", a dynamic Azure CycleCloud and Slurm cluster scaling on-demand to hundreds of GPUs with 7 PB of whole-slide imaging on Azure Managed Lustre; ran 1.5M jobs in 2025.
- Grew the environment from 5 to 40+ ML researchers across four NVIDIA generations (Pascal, Volta, Ampere, Hopper) and from on-prem to Azure and AWS.
- Helped hire the early management and engineering staff, including ML, infrastructure, and platform leads.
- Now migrating Paige's training and inference infrastructure into Tempus's GCP environment as its pathology models fold into Tempus's oncology foundation-model effort.

### HPC Engineer
**Memorial Sloan Kettering Cancer Center, New York City**
*2018–2022 (concurrent with Paige.AI)*

- Designed and built a 100-GPU DGX-1 cluster with Cisco RoCE networking and Pure Storage FlashBlade for high-throughput AI/ML workloads.
- Expanded storage to 4 PB of object (S3/Qumulo) and 500 TB of Pure FlashBlade by migrating from a flat to a tiered model based on data temperature.
- Evaluated and helped acquire a turn-key scientific datacenter facility.

### Computing and Software Systems Research Engineer
**California Institute of Technology High Energy Physics – CMS, Pasadena, California**
*2015–2018*

- Principal administrator of the Caltech Tier-2 cluster for the Compact Muon Solenoid experiment at CERN's Large Hadron Collider, one of the largest production scientific computing environments in physics.
- Operated a 7,300-slot HTCondor scheduling system with 4.5 PB of storage in continuous collaboration with Fermilab, CERN, and the Open Science Grid.
- Redesigned the core network topology into a tiered model to minimize latency and increase redundancy for distributed scientific workflows.
- Developed a state-of-the-art SDN testbed for testing scientific workflows via contributions to the ESnet project.
- Presenter and technical exercise contributor to ESnet network demonstrations at Supercomputing; also presented at HEPiX and OSG/HTCondor Week.

### Earlier Career

**Duke University, Durham, NC** — *2011–2015* — Principal Unix/Linux and network analyst on the IT Operations Management team. Owned monitoring, alerting, and change management across all academic and enterprise infrastructure; principal administrator for application performance and 24/7 NOC alerting systems.

**FedEx, Memphis, TN** — *2005–2011* — Senior Technical Analyst and Technical Analyst supporting Unix/Linux production systems for global logistics, SCADA infrastructure for sorting facilities, and the [www.fedex.com](https://www.fedex.com) distributed infrastructure. Started as Intern II in 2005 with the Systems Administration and Consulting group.

**Contractor and university work, 2000–2005** — Building network and wifi upgrades, departmental websites, and a business backup solution for critical data.

---

## Technical Expertise

NVIDIA DGX and GPU cluster architecture across Pascal, Volta, Ampere, Hopper, and Blackwell. Slurm, Azure CycleCloud, HTCondor, Kueue, and Kubernetes for scheduling and orchestration. InfiniBand, RoCE, NVLink/NVSwitch, GPUDirect RDMA, NCCL, and DOCA for high-performance fabrics. Lustre, Weka, GPFS, NetApp, Pure, and S3/Blob for high performance storage and data archival at petabyte scale. Azure, AWS, and GCP with Terraform, Packer, and Ansible. Network performance and systems debugging on Linux, and automation with mostly shell and Python.

---

## Publications

Full list on the [Publications](/publications/) page.

---
