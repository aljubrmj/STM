<!--
Hey, thanks for using the awesome-readme-template template.  
If you have any enhancements, then fork this project and create a pull request 
or just open an issue with the label "enhancement".

Don't forget to give this project a star for additional support ;)
Maybe you can mention me or this repo in the acknowledgements too
-->
<div align="center">

  <img src="assets/stm_logo.png" alt="logo" width="500" height="auto" />
  
<!--   <p>
    Stanford Temperature Model 
    You can directly access this webapp online at [http://www.stanford-temperature-model.com/](http://www.stanford-temperature-model.com/)
  </p> -->
  
  
<!-- Badges -->
<!-- <p>
  <a href="https://github.com/Louis3797/awesome-readme-template/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Louis3797/awesome-readme-template" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/Louis3797/awesome-readme-template" alt="last update" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/network/members">
    <img src="https://img.shields.io/github/forks/Louis3797/awesome-readme-template" alt="forks" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/stargazers">
    <img src="https://img.shields.io/github/stars/Louis3797/awesome-readme-template" alt="stars" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/issues/">
    <img src="https://img.shields.io/github/issues/Louis3797/awesome-readme-template" alt="open issues" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/Louis3797/awesome-readme-template.svg" alt="license" />
  </a>
</p> -->
   
<!-- <h4>
    <a href="https://github.com/Louis3797/awesome-readme-template/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/Louis3797/awesome-readme-template">Documentation</a>
  <span> · </span>
    <a href="https://github.com/Louis3797/awesome-readme-template/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/Louis3797/awesome-readme-template/issues/">Request Feature</a>
  </h4> -->
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
- [Getting Started](#toolbox-getting-started)
- [Contributing](#wave-contributing)
- [License](#warning-license)
- [Contact](#handshake-contact)
  
<!-- About the Project -->
## :star2: About the Project
This repository is the webapp where the Stanford thermal Earth model is deployed. Here, we briefly describe the original project behind this work[^1][^2]. 

Provided here are various forms of the Stanford Thermal Earth Model, as well as the data and methods used for its creation. The predictions produced by this model were visualized in two-dimensional spatial maps across the modeled depths (0-7 km) for the conterminous United States. The thermal earth model is made available as an application programming interface (API) and as feature layers on ArcGIS, which are both provided via links below.

A data-driven spatial interpolation algorithm based on physics-informed graph neural networks was used to develop these national temperature-at-depth maps. The model satisfied the three-dimensional heat conduction law by predicting subsurface temperature, surface heat flow, and rock thermal conductivity. Many physical quantities, including bottomhole temperature, depth, geographic coordinates, elevation, sediment thickness, magnetic anomaly, gravity anomaly, gamma-ray flux of radioactive elements, seismicity, and electric conductivity were used as model inputs. Surface heat flow, temperature, and thermal conductivity predictions were constructed for depths of 0-7 km at an interval of 1 km with spatial resolution of 18 km2 per grid cell. The model showed superior temperature, surface heat flow and thermal conductivity mean absolute errors of 4.8C, 5.817 mW/m2 and 0.022 W/(C-m), respectively.

<!-- Screenshots -->
<!-- ### :camera: Screenshots

<div align="center"> 
  <img src="https://placehold.co/600x400?text=Your+Screenshot+here" alt="screenshot" />
</div>


<!-- TechStack -->
<!-- ### :space_invader: Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
    <li><a href="https://nextjs.org/">Next.js</a></li>
    <li><a href="https://reactjs.org/">React.js</a></li>
    <li><a href="https://tailwindcss.com/">TailwindCSS</a></li>
  </ul>
</details> -->

<!-- <details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
    <li><a href="https://expressjs.com/">Express.js</a></li>
    <li><a href="https://go.dev/">Golang</a></li>
    <li><a href="https://nestjs.com/">Nest.js</a></li>
    <li><a href="https://socket.io/">SocketIO</a></li>
    <li><a href="https://www.prisma.io/">Prisma</a></li>    
    <li><a href="https://www.apollographql.com/">Apollo</a></li>
    <li><a href="https://graphql.org/">GraphQL</a></li>
  </ul>
</details> -->

<!-- <details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.mysql.com/">MySQL</a></li>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
    <li><a href="https://redis.io/">Redis</a></li>
    <li><a href="https://neo4j.com/">Neo4j</a></li>
    <li><a href="https://www.mongodb.com/">MongoDB</a></li>
  </ul>
</details> -->

<!-- <details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
    <li><a href="https://www.jenkins.io/">Jenkins</a></li>
    <li><a href="https://circleci.com/">CircleCLI</a></li>
  </ul>
</details> -->

<!-- Features -->
<!-- ### :dart: Features

- Feature 1
- Feature 2
- Feature 3 -->

<!-- Color Reference -->
<!-- ### :art: Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Primary Color | ![#222831](https://via.placeholder.com/10/222831?text=+) #222831 |
| Secondary Color | ![#393E46](https://via.placeholder.com/10/393E46?text=+) #393E46 |
| Accent Color | ![#00ADB5](https://via.placeholder.com/10/00ADB5?text=+) #00ADB5 |
| Text Color | ![#EEEEEE](https://via.placeholder.com/10/EEEEEE?text=+) #EEEEEE |
 -->

<!-- Env Variables -->
<!-- ### :key: Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY` --> 

<!-- Getting Started -->
## 	:toolbox: Getting Started

### :eight_spoked_asterisk: Run on Google Colab (No Local Installation)
You can directly access this webapp online at [http://www.stanford-temperature-model.com/](http://www.stanford-temperature-model.com/)

<!-- Prerequisites -->
### :gear: Local Installation

1. Create a Python 3.8 or newer virtual environment
   *If you're not sure how to create a suitable Python environment, the easiest way is using [Miniconda](https://docs.conda.io/en/latest/miniconda.html). On a Mac, for example, you can install Miniconda using [Homebrew](https://brew.sh/):*

    ```
    brew install miniconda
    ```

    *Then you can create and activate a new Python environment by running:*

    ```
    conda create -n my-package python=3.9
    conda activate my-package
    ```
2. Clone the STM github repositary, change directories, and install the required Python packages by running the following:

```bash
git clone https://github.com/aljubrmj/STM
cd STM
pip install -r requirements.txt
```
<!-- Running Tests -->
### :test_tube: Running Locally

To run locally, run the following command in the STM directory

```bash
  python app.py
```

<!-- Usage -->
<!-- ## :eyes: Usage

Use this space to tell a little more about your project and how it can be used. Show additional screenshots, code samples, demos or link to other resources.


```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
``` -->

<!-- Roadmap -->
<!-- ## :compass: Roadmap

* [x] Todo 1
* [ ] Todo 2 -->


<!-- Contributing -->
## :wave: Contributing

<!-- <a href="https://github.com/Louis3797/awesome-readme-template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Louis3797/awesome-readme-template" />
</a> -->


Contributions are always welcome!

<!-- See `contributing.md` for ways to get started. -->


<!-- Code of Conduct -->
<!-- ### :scroll: Code of Conduct

Please read the [Code of Conduct](https://github.com/Louis3797/awesome-readme-template/blob/master/CODE_OF_CONDUCT.md) -->

<!-- FAQ -->
<!-- ## :grey_question: FAQ

- Question 1

  + Answer 1

- Question 2

  + Answer 2 -->


<!-- License -->
## :warning: License

Distributed under the MIT License. See LICENSE.txt for more information.


<!-- Contact -->
## :handshake: Contact

Mohammad Aljubran - [LinkedIn](https://www.linkedin.com/in/mohammad-aljubran) - [Scholar](https://scholar.google.com/citations?user=7-YoZS8AAAAJ&hl=en)- aljubrmj@stanford.edu; m.j.aljubran@gmail.com

<!-- Acknowledgments -->
<!-- ## :gem: Acknowledgements

Correlations used in this model across both upstream and downstream components are based on GETEM and GEOPHIRES. -->

[^1]: Aljubran, M. J., & Horne, R. N. (2024). Thermal Earth Model for the Conterminous United States Using an Interpolative Physics-Informed Graph Neural Network (InterPIGNN). Preprint. arXiv:2403.09961
[^2]: Stanford University. (2024). Stanford Thermal Earth Model for the Conterminous United States [data set]. Retrieved from https://dx.doi.org/10.15121/2324793.
