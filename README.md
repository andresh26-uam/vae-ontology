[VAE Ontology](https://w3id.org/def/vaeontology)
===================

The purpose of the [VAE Ontology](https://w3id.org/def/vaeontology) is to represent nomenclature and formalize value reasoning for value-aware systems. The emerging field of *value awareness engineering* enforces different relevant value-related duties that our agents should perform to achieve value-aligned outcomes and, ultimately, respond to a value-aware behaviour. In this work we follow the [NeOn methodology](https://oeg.fi.upm.es/index.php/en/methodologies/59-neon-methodology/index.html) to develop an initial ontology that ambitions to link some of the proposed ideas in this field. The scenario-based method applies the tasks of: ontology specification, scheduling, reuse of applicable ontologies and knowledge organization systems, conceptualization and formalization, implementation, evaluation, upgrade and documentation.

![image](https://github.com/andresh26-uam/vae-ontology/blob/main/diagrams/diagram_vaeontology_ADHOC_White.png)

Reused ontologies include the pioneer [ValueNet](https://github.com/StenDoipanni/ValueNet), an OWL ontology network representing values from different theories, focusing in detecting value-related situations in the linguistic domain. That network heavily relies on upper level ontology [DOLCE](https://doi.org/10.3233%2Fao-210259), also reused here. Lastly, to represent different policies that our AI agents should abide to in order to certify their awareness for values, we use the [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/) ontology.

# VAE ontology core and cases
The VAE ontology is fundamentally implemented in a central module that can be imported to adapt theories of value-alignment.

[VAE](https://w3id.org/def/vaeontology) ``https://w3id.org/def/vaeontology`` <br/>

## Implemented VAE proposals as ontologies

So far we have implemented parts of the following proposals from the VAE community:
- (VAEMS) Ontology on "Synthesis and properties of optimally value-aligned normative systems", Montes, N., Sierra, C. (2022).
- (VAEODI) Ontology on "A computational framework of human values for ethical AI" by Nardine Osman and Mark d’Inverno (2023)
- (VAEMVNDM) Ontology on "Moral Values in Norm Decision Making", Serramia, M. et al. (2018).

## Prefixes
[VAEMS](https://w3id.org/def/vaeontology_montes_sierra) ``https://w3id.org/spice/SON/SchwartzValues`` <br/>
[VAEODI](https://w3id.org/def/vaeontology_osman_dInverno) ``https://w3id.org/def/vaeontology_osman_dInverno`` <br/>
[VAEMVNDM](https://w3id.org/def/vaeontology_moral_values_in_norm_DM) ``https://w3id.org/def/vaeontology_moral_values_in_norm_DM`` <br/>

# References
- ([NeOn](https://oeg.fi.upm.es/index.php/en/methodologies/59-neon-methodology/index.html)) Suárez-Figueroa, Mari Carmen (2010). NeOn Methodology for Building Ontology Networks: Specification, Scheduling and Reuse. Thesis (Doctoral), Facultad de Informática (UPM). https://doi.org/10.20868/UPM.thesis.3879.
- ([ValueNet](https://github.com/StenDoipanni/ValueNet)) De Giorgis, S., Gangemi, A., Damiano, R.: Basic human values and moral foundations theory in valuenet ontology. In: International Conference on Knowledge Engineering and Knowledge Management. pp. 3–18. Springer (2022)
- ([DOLCE](https://doi.org/10.3233%2Fao-210259)) Borgo, S., Ferrario, R., Gangemi, A., Guarino, N., Masolo, C., Porello, D., Sanfilippo, E.M., Vieu, L.: DOLCE: A descriptive ontology for linguistic and cognitive engineering. Applied Ontology 17(1), 45–69 (mar 2022) [https://doi.org/10.3233%2Fao-210259](https://doi.org/10.3233%2Fao-210259)
- ([ODRL](https://www.w3.org/TR/odrl-model/)) Ianella, R., Villata, S.: ODRL information model 2.2. W3C Recommendation, W3C (Feb 2018) [https://www.w3.org/TR/odrl-model/](https://www.w3.org/TR/odrl-model/)
- Montes, N., Sierra, C.: Synthesis and properties of optimally value-aligned normative systems. Journal of Artificial Intelligence Research 74, 1739–1774 (2022). [https://doi.org/10.1613/jair.1.13487](https://doi.org/10.1613/jair.1.13487)
- Osman, N., d’Inverno, M.: A computational framework of human values for ethical ai (2023) [https://arxiv.org/abs/2305.02748](https://arxiv.org/abs/2305.02748)
- Marc Serramia, Maite Lopez-Sanchez, Juan A. Rodriguez-Aguilar, Manel Rodriguez, Michael Wooldridge, Javier Morales, and Carlos Ansotegui. 2018. Moral Values in Norm Decision Making. In Proceedings of the 17th International Conference on Autonomous Agents and MultiAgent Systems (AAMAS '18). International Foundation for Autonomous Agents and Multiagent Systems, Richland, SC, 1294–1302. [https://dl.acm.org/doi/10.5555/3237383.3237891](https://dl.acm.org/doi/10.5555/3237383.3237891)

