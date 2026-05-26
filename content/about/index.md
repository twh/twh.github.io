---
title: "About"
date: 2026-05-08
showTableOfContents: false
---

I keep large training runs alive.

For the last seven years that has meant pathology foundation models at
Paige.AI and now Tempus. Before that, it meant the Compact Muon Solenoid
experiment at CERN's Large Hadron Collider, where I ran the Caltech
Tier-2 — one of the U.S. compute sites the physics collaboration depends
on to reconstruct collision events. Before that, enterprise systems at
Duke and Unix production at FedEx.

The thread is not "AI" or "physics." It is production infrastructure for
missions where the cost of a failed run is high — months of physicist
time, or weeks of GPU-hours on a billion-parameter model. The skills
transfer better than people assume. Scheduling, storage tiering, network
fabric, observability, change management under pressure — the LHC people
and the foundation-model people are solving the same problem at different
scales of data and different shapes of compute.

What I'm working on now is the migration of Paige's pathology training
and inference into Tempus's GCP environment, while continuing to scale
the existing Azure footprint. The interesting problems are around
checkpoint resharding across heterogeneous fabrics, training reliability
at multi-node scale, and storage architectures that can hold 7 PB of
whole-slide imaging hot enough for randomized I/O during training.

Outside Tempus I am most interested in the infrastructure layer of
biological and scientific foundation models — autonomous wet-lab
platforms, structural biology training pipelines, and the next generation
of clinical AI where the data is larger than the model. If that is what
you're building, [say hello](mailto:twh@waynehendricks.com).

The [CV](/cv/) has the full chronology. Publications and acknowledgements
[here](/publications/).
