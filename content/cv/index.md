---
title: "CV"
date: 2026-05-08
showTableOfContents: true
---

[Download PDF version](/files/wayne-hendricks-cv.pdf)

---

# Thomas Wayne Hendricks

---

## Professional Summary

Principal HPC engineer specializing in foundation model training infrastructure for clinical and scientific AI. Currently a Senior HPC Engineer at Tempus in New York City, where I lead GPU and storage infrastructure behind histopathology foundation models. Joined through the September 2025 $81M acquisition of Paige.AI, where I was the sole HPC engineer through the company's growth from 5 to 40+ machine learning users and helped fill the early engineering staff. Previously principal administrator of the Caltech CMS Tier-2 cluster for the Large Hadron Collider, operating 7,300 HTCondor slots and 4.5 PB of storage in production collaboration with CERN, Fermilab, and the Open Science Grid.

Distinctive combination of regulated clinical AI infrastructure (FDA-cleared products built on top of systems I designed) and distributed scientific computing at extreme scale (one of the largest production HTCondor deployments in academic physics). Looking for principal or founding-engineering roles at AI/bio companies advancing scientific and biological foundation models, autonomous lab platforms, or frontier-scale training infrastructure.

---

## Selected Achievements

- Sole HPC engineer at Paige.AI (2022–2025) through the $81M acquisition by Tempus AI in September 2025.
- Built the GPU and storage infrastructure behind the [Virchow2](https://arxiv.org/abs/2408.00738) and [PRISM](https://arxiv.org/abs/2405.10254) histopathology foundation models, both state-of-the-art in clinical AI for pathology.
- Scaled clinical AI training infrastructure across four NVIDIA generations: Pascal, Volta, Ampere, and Hopper.
- Designed and operated multi-cloud HPC environments on Azure and AWS with Lustre, Weka, and NetApp storage.
- Principal administrator of the Caltech CMS Tier-2 cluster for the LHC: 7,300 HTCondor slots, 4.5 PB of storage.
- Built the 100-GPU DGX-1 AI/ML cluster at Memorial Sloan Kettering Cancer Center with Cisco RoCE and Pure Storage FlashBlade.
- Conducted technical interviews from individual contributor through VP level, helping fill the early engineering staff at Paige.AI.

---

## Career History

### Senior HPC Engineer
**Tempus AI (formerly Paige.AI), New York City**
*2022–Present*

- **Sole HPC engineer at Paige.AI through the $81M acquisition by Tempus AI in September 2025.** Owned end-to-end GPU, storage, scheduling, and multi-cloud infrastructure for clinical foundation model training.
- Built and scaled the GPU training infrastructure behind the Virchow2 and PRISM histopathology foundation models, both state-of-the-art in clinical AI for pathology.
- Architected a dynamic Azure CycleCloud cluster that scales on-demand to hundreds of GPU nodes; executed 1.5M Slurm jobs in 2025.
- Managed 7 PB of whole-slide image data in Azure Blob Storage fronted by Azure Managed Lustre for high-throughput training I/O.
- Scaled training infrastructure from 5 to 40+ ML users while moving from Pascal/Volta on-prem GPUs to Ampere/Hopper systems across Azure and AWS.
- Integrated Dask and Prefect with the Slurm API for automated job orchestration; deployed cloud scheduling system used across the organization.
- Key computing infrastructure resource to multiple AI/ML research and engineering teams.
- Continued in this role through the Tempus integration, where Paige's pathology foundation models are being incorporated into Tempus's broader oncology foundation model effort.

### HPC Engineer
**Memorial Sloan Kettering Cancer Center, New York City**
*2018–2022*

- Designed and built a 100-GPU DGX-1 cluster with Cisco RoCE networking and Pure Storage FlashBlade for high-throughput AI/ML workloads.
- Conducted technical interviews from individual contributor to VP level and helped fill most of the early engineering staff at Paige.
- Served as an engineering consultant resource to the Research Computing and HPC teams.
- Expanded storage to 4 PB of object (S3/Qumulo) and 500 TB of Pure FlashBlade by migrating from a flat to a tiered model based on data temperature.
- Assisted with the acquisition and leasing of a turn-key scientific datacenter facility.

### Computing and Software Systems Research Engineer
**California Institute of Technology High Energy Physics – CMS, Pasadena, California**
*2015–2018*

- Principal administrator of the Caltech Tier-2 cluster for the Compact Muon Solenoid experiment at CERN's Large Hadron Collider — one of the largest production scientific computing environments in physics.
- Operated a 7,300-slot HTCondor scheduling system with 4.5 PB of storage in continuous collaboration with Fermilab, CERN, and the Open Science Grid.
- Redesigned the core network topology into a tiered model to minimize latency and increase redundancy for distributed scientific workflows.
- Developed a state-of-the-art SDN testbed for testing scientific workflows via contributions to the ESnet project.
- Deployed an R&D Ceph cluster for testing advanced storage features and contributing to the XrootD project.
- Managed an annual hardware budget of $150k for cluster maintenance and refreshes.
- Presented research and infrastructure work at Supercomputing, HEPiX, OSG/HTCondor Week, and NVIDIA GTC.

### Earlier Career

**Duke University, Durham, NC** — *2011–2015* — Principal Unix/Linux and network analyst on the IT Operations Management team. Owned monitoring, alerting, and change management across enterprise infrastructure; principal administrator for 24/7 NOC alerting systems and the 20k-endpoint VoIP environment.

**FedEx, Memphis, TN** — *2005–2011* — Senior Technical Analyst and Technical Analyst supporting Unix/Linux production systems for global logistics, SCADA infrastructure for lights-out sorting facilities, and the [www.fedex.com](https://www.fedex.com) distributed infrastructure. Started as Intern II in 2005 with the Systems Administration and Consulting group.

**Contractor and college work, 2000–2005** — Building network and wifi upgrades, departmental websites, and a business backup solution for critical data.

---

## Education & Training

**BaSc in Information Systems Infrastructure/Security**
ITT, Memphis, TN.

**Corporate Training Courses:**
Programming Perl, Linux Systems Administration, Managing Security in Software Projects, Firewall Techniques.

**Conferences:**
Regular attendee at Duke TechExpo, HEPiX, OSG/HTCondor Week, Supercomputing, ISC, NVIDIA GTC.

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

---

## Publications and Acknowledgments

See the [Publications](/publications/) page for the full list with links.

---