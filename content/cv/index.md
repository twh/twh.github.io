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

Senior HPC engineer with 20 years of experience building large-scale computing infrastructure across high-energy physics, oncology AI, and foundational model training. Experienced across multiple GPU generations and petabyte-scale parallel storage, with hands-on depth in Slurm and HTCondor scheduling at scale. Infrastructure contributor to the groundbreaking Virchow2 and PRISM histopathology models at Paige.AI/Tempus. Previously built and operated the Caltech CMS Tier-2, a 7,300-slot HTCondor cluster with 4.5 PB of storage supporting the Large Hadron Collider.

---

## Career History

### Senior HPC Engineer
**Tempus AI (formerly Paige.AI), New York City**
*2022–Present*

- Sole HPC engineer focusing on AI/ML imagery workflows on NVIDIA GPUs.
- Architected a dynamic Azure CycleCloud cluster that scales on-demand to hundreds of GPU nodes; executed 1.5M Slurm jobs in 2025.
- Managed 7 PB of whole-slide image data in Azure Blob Storage fronted by Azure Managed Lustre for high-throughput training I/O.
- Key computing infrastructure resource to multiple AI/ML teams.
- Deployed cloud scheduling system and scaled from 5 users to 40+.
- Scaled from Pascal/Volta GPUs to Ampere/Hopper GPU and CPU systems.
- Integrated Dask and Prefect tools with the Slurm API for automated job scheduling.
- Assisted with the development of two ground-breaking histopathology foundational models.
- Helped scale and grow Paige until the $81M acquisition by Tempus AI in Sept 2025.

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

- Principal administrator of the Caltech Tier2 cluster for the Compact Muon Solenoid at CERN's Large Hadron Collider.
- Deployed and maintained a 7,300 slot HTCondor scheduling system with 4.5 PB of storage.
- Collaborated with Fermilab, CERN, and other sites on LHC and Open Science Grid compute infrastructure.
- Managed a budget of $150k per year for hardware maintenance and refreshes.
- Developed a state-of-the-art SDN testbed for testing scientific workflows via contribution to ESnet.
- Redesigned the core network topology into a tiered model to minimize latency and increase redundancy.
- Deployed an R&D Ceph cluster for testing advanced features and contributing to the XrootD project.
- Presented at various conferences and institutions showcasing the work done by the Caltech HEP team.

### Systems Analyst, IT Operations Management
**Duke University, Durham, North Carolina**
*2011–2015*

- Principal Unix/Linux and network analyst on a small operations team that managed all university systems and applications.
- Conducted change management, incident management, operations monitoring, and documentation for all enterprise applications.
- Principal administrator for monitoring/metrics and mission critical 24/7 NOC alerting systems.
- Acted as a liaison to the Network/VoIP engineering teams and technical advisor to academic, research, and business teams.
- Coded large screen dashboard displays in Perl for ServiceNow, Tableau, CA Spectrum, and other APIs.
- Led evaluation of monitoring and metrics products for 20k endpoint VoIP infrastructure.

### Senior Technical Analyst
**FedEx, Memphis, Tennessee**
*2007–2011*

- Provided production support for Unix/Linux sorting automation and command-and-control hosts.
- Deployed and maintained highly available SCADA systems critical to global logistics operations.
- Advised multiple teams on operating systems, DNS, web, monitoring, automation, and security.
- Constructed monitoring and response solution for worldwide critical SCADA systems.
- Designed and deployed systems for a new full-automated lights-out facility.
- Supported 900MHz wireless and handheld device infrastructure.

### Technical Analyst
**FedEx, Memphis, Tennessee**
*2005–2007*

- Assisted with the day-to-day operation of the www.fedex.com distributed infrastructure.
- Monitored production Linux/FreeBSD/Solaris systems across DMZ, ZMD, and backend.
- Provided first level support for all fedex.com C and Java/Weblogic applications.
- Organized and managed emergency technical conference bridges during incidents.

### Intern II
**FedEx, Memphis, Tennessee**
*2005*

- Interned with the Systems Administration and Consulting group.
- Assisted with the implementation of new data center infrastructure.
- Retired a legacy request queue system by migrating to a new one.

### Contractor / College Student
*2000–2005*

- Evaluated, designed, and implemented a building network and wifi upgrade.
- Constructed and maintained a new university departmental website.
- Developed and deployed a business backup solution for critical data.

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