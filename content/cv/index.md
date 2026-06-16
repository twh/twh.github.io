---
title: "CV"
date: 2026-05-08
showTableOfContents: true
---

# Thomas Wayne Hendricks

[GitHub](https://github.com/twh) ·
[Google Scholar](https://scholar.google.com/citations?hl=en&user=R2H2QjwAAAAJ) ·
[ORCID](https://orcid.org/0000-0001-9111-8968) ·
[twh@waynehendricks.com](mailto:twh@waynehendricks.com)

---

## Professional Summary

Principal HPC engineer specializing in foundation model training infrastructure for clinical and scientific AI. Currently a Senior HPC Engineer at Tempus in New York City, where I lead GPU and storage infrastructure behind histopathology foundation models. Joined Tempus through the September 2025 $81M acquisition of Paige.AI, where I had been the sole HPC engineer from 2018 through the acquisition, scaling the company from 5 to 40+ ML users and helping fill the early engineering staff. Previously principal administrator of the Caltech CMS Tier-2 cluster for the Large Hadron Collider, operating 7,300 HTCondor slots and 4.5 PB of storage in production collaboration with CERN, Fermilab, and the Open Science Grid.

Distinctive combination of regulated clinical AI infrastructure (FDA-cleared products built on top of systems I designed) and distributed scientific computing at extreme scale (one of the largest production HTCondor deployments in academic physics). Looking for principal or founding-engineering roles at AI/bio companies advancing scientific and biological foundation models, autonomous lab platforms, or frontier-scale training infrastructure.

---

## Selected Achievements

- Sole HPC engineer at Paige.AI (2018–2025) through the $81M acquisition by Tempus AI in September 2025.
- Built the GPU and storage infrastructure behind the [Virchow](https://arxiv.org/abs/2309.07778), [Virchow2](https://arxiv.org/abs/2408.00738), [PRISM](https://arxiv.org/abs/2405.10254), and [PRISM2](https://arxiv.org/abs/2506.13063) histopathology foundation models.
- Acknowledged infrastructure contributor in the [Virchow](https://arxiv.org/abs/2309.07778) (arXiv, 2023; later published in [*Nature Medicine*](https://www.nature.com/articles/s41591-024-03141-0)) and [Virchow2](https://arxiv.org/abs/2408.00738) (arXiv, 2024) preprints.
- Scaled clinical AI training infrastructure across four NVIDIA generations: Pascal, Volta, Ampere, and Hopper.
- Designed and operated multi-cloud HPC environments on Azure and AWS with Lustre, Weka, and NetApp storage.
- Principal administrator of the Caltech CMS Tier-2 cluster for the LHC: 7,300 HTCondor slots, 4.5 PB of storage.
- Built the 100-GPU DGX-1 AI/ML cluster at Memorial Sloan Kettering Cancer Center with Cisco RoCE and Pure Storage FlashBlade.
- Helped hire the early management and engineering staff at Paige.AI, including ML, infrastructure, and platform leads.

---

## Career History

### Senior HPC Engineer
**Tempus AI (formerly Paige.AI), New York City**
*2018–Present*

- **Sole HPC engineer at Paige.AI from 2018 through the September 2025 Tempus acquisition.** Owned end-to-end GPU, storage, scheduling, and multi-cloud infrastructure for clinical foundation model training.
- Built and scaled the GPU training infrastructure behind the Virchow, Virchow2, PRISM, and PRISM2 histopathology foundation models.
- Architected a dynamic Azure CycleCloud cluster that scales on-demand to hundreds of GPU nodes; executed 1.5M Slurm jobs in 2025.
- Managed 7 PB of whole-slide image data in Azure Blob Storage fronted by Azure Managed Lustre for high-throughput training I/O.
- Scaled training infrastructure from 5 to 40+ ML users while moving from Pascal/Volta on-prem GPUs to Ampere/Hopper systems across Azure and AWS.
- Integrated Dask and Prefect with the Slurm API for automated job orchestration; deployed cloud scheduling system used across the organization.
- Key computing infrastructure resource to multiple AI/ML research and engineering teams.
- Continued in this role through the Tempus integration, where Paige's pathology foundation models are being incorporated into Tempus's broader oncology foundation model effort.
- Helping migrate Paige's training and inference infrastructure into Tempus's GCP environment.

### HPC Engineer
**Memorial Sloan Kettering Cancer Center, New York City**
*2018–2022 (concurrent with Paige.AI)*

- Designed and built a 100-GPU DGX-1 cluster with Cisco RoCE networking and Pure Storage FlashBlade for high-throughput AI/ML workloads.
- Served as an engineering consultant resource to the Research Computing and HPC teams.
- Expanded storage to 4 PB of object (S3/Qumulo) and 500 TB of Pure FlashBlade by migrating from a flat to a tiered model based on data temperature.
- Assisted with the acquisition and leasing of a turn-key scientific datacenter facility.

### Computing and Software Systems Research Engineer
**California Institute of Technology High Energy Physics – CMS, Pasadena, California**
*2015–2018*

- Principal administrator of the Caltech Tier-2 cluster for the Compact Muon Solenoid experiment at CERN's Large Hadron Collider, one of the largest production scientific computing environments in physics.
- Operated a 7,300-slot HTCondor scheduling system with 4.5 PB of storage in continuous collaboration with Fermilab, CERN, and the Open Science Grid.
- Redesigned the core network topology into a tiered model to minimize latency and increase redundancy for distributed scientific workflows.
- Developed a state-of-the-art SDN testbed for testing scientific workflows via contributions to the ESnet project.
- Deployed an R&D Ceph cluster for testing advanced storage features and contributing to the XrootD project.
- Managed an annual hardware budget of $150k for cluster maintenance and refreshes.
- Presenter and technical exercise contributor to ESnet network demonstrations at Supercomputing.
- Presented research and infrastructure work at HEPiX and OSG/HTCondor Week.

### Earlier Career

**Duke University, Durham, NC** — *2011–2015* — Principal Unix/Linux and network analyst on the IT Operations Management team. Owned monitoring, alerting, and change management across enterprise infrastructure; principal administrator for 24/7 NOC alerting systems and the 20k-endpoint VoIP environment.

**FedEx, Memphis, TN** — *2005–2011* — Senior Technical Analyst and Technical Analyst supporting Unix/Linux production systems for global logistics, SCADA infrastructure for lights-out sorting facilities, and the [www.fedex.com](https://www.fedex.com) distributed infrastructure. Started as Intern II in 2005 with the Systems Administration and Consulting group.

**Contractor and college work, 2000–2005** — Building network and wifi upgrades, departmental websites, and a business backup solution for critical data.

---

## Technical Experience

| Category | Technologies |
|---|---|
| **Schedulers** | Slurm, HTCondor, Kueue, OpenMPI, NVIDIA tools |
| **GPU / Compute** | NVIDIA DGX, Cisco UCS, Supermicro, Dell, HP Proliant |
| **Storage** | Lustre, Weka, GPFS, Ceph, ZFS, DRBD, Gluster, HDFS, NetApp, Qumulo, Pure |
| **Cloud** | Azure, AWS, GCP, VMware, KVM/libvirt, OpenStack |
| **Networking** | Mellanox, Cisco NXOS/IOS, Arista, Dell/Force10, EdgeCore/whitebox, DOCA, NCCL |
| **IaC / Config** | Terraform, Packer, Ansible, Puppet, Salt, Git, GitHub, GitLab |
| **Monitoring** | Prometheus, Grafana, InfluxDB, DataDog, Ganglia, Nagios, PagerDuty, SumoLogic |
| **OS** | RHEL/Rocky/Alma, FreeBSD, Ubuntu, Oracle/Sun Solaris, macOS |
| **Security / IdM** | SSSD, OpenLDAP, Okta, SentinelOne, nftables/pf, CIS Hardening |
| **Languages** | Python, Bash/shell, Perl, Ruby |
| **IDEs / Coding Tools** | Codex, Claude Code, Cursor, VS Code |

---

## Publications and Acknowledgments

See the [Publications](/publications/) page for the full list with links.

---