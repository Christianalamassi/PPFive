import streamlit as st
import matplotlib.pyplot as plt


def summery_page():
    st.write("### Quick Summary of the Project ")
    st.write("---")

    st.info(
        '**General Information**\n'
        '* Definition: Powdery mildew of sweet and sour cherry is caused by Podosphaera clandestina, an obligate biotrophic fungus. Mid- and late-season sweet cherry (Prunus avium) cultivars are commonly affected, rendering them unmarketable due to the covering of white fungal growth on the cherry surface. Season-long disease control of both leaves and fruit is critical to minimize overall disease pressure in the orchard and consequently to protect developing fruit from accumulating spores on their surfaces.\n'
        '* Symptoms: On leaves, powdery mildew appears as patches of white, powdery, or felt-like fungal growth. Severely affected leaves and shoots are often puckered or distorted.\n'
        '* Conditions favor disease: The fungus does not need free water to thrive. High humidity and temperatures of 21°C to 26°C favor the disease. Spore dispersal is diurnal, with spore concentrations peaking late morning to early afternoon (Grove 1998, Glawe 2008.\n'
        '* Cultural Control: Consider post-harvest application of fungicides to prevent buildup of mildew on foliage and reduce the amount of overwintering inoculum.  For these late season sprays it is best to select products that have a low risk of resistance, such as sulphur, bicarbonate or summer oil.' 
        )

    st.success (
    '**The business requirements of the project**\n'
    '* The client is interested in conducting a study to distinguish between healthy leaves or moldy leaves.\n'
    '* The client is interested in knowing whether a given leaf contains mold or not.'
    )

    st.write('For additional information, please visit [README file](https://github.com/Christianalamassi/PPFive/blob/main/README.md).')