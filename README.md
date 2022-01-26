<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Codecov branch][codecov-shield]][codecov-url]
[![PyPI - Wheel][pypi-shield]][pypi-url]
[![build-status][documentation-generation-shield]][documentation-generation-url]
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/karafra/steg-utility">
    <img src="https://t3.ftcdn.net/jpg/03/08/05/36/240_F_308053686_1GW2ZhfMSiEGBAM9QEFlm497J6qoUKYL.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Steganography utility</h3>

  <p align="center">
    Simple steganography command line utility
    <br />
    <a href="https://karafra.github.io/steg-utility/ "><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/karafra/steg-utility/issues">Report Bug</a>
    ·
    <a href="https://github.com/karafra/steg-utility/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Simple utility used for image based steganography. Encryption method is least significant byte. 
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [OpenCv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
* [NumPy](https://numpy.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To setup this project follow these simple steps.
### Prerequisites

To run this project you need copy of Python3
* npm
  ```sh
  sudo apt-get update
  sudo apt-get install python3.8
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/karafra/steg-utility.git
   ```
2. Install python packages
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
CLI supports two modes (encode/decode). 

Encode:
```sh
  steganography -m decode -i output.png
```
Decode:
```sh
steganography -m encode  -i input.png -o output.png -p "Super secret message"
```

_For more examples, please refer to the [Documentation](https://karafra.github.io/steg-utility/)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap
See the [open issues](https://github.com/karafra/steg-utility/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Apache 2.0 License. See <a href="LICENSE"> LICENSE </a>for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@karafro](https://twitter.com/karafro) - dariusKralovic@protonmail.com

Project Link: [https://github.com/karafra/steg-utility](https://github.com/karafra/steg-utility)

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/karafra/steg-utility.svg?style=for-the-badge
[contributors-url]: https://github.com/karafra/steg-utility/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/karafra/steg-utility.svg?style=for-the-badge
[forks-url]: https://github.com/karafra/steg-utility/network/members
[stars-shield]: https://img.shields.io/github/stars/karafra/steg-utility.svg?style=for-the-badge
[stars-url]: https://github.com/karafra/steg-utility/stargazers
[issues-shield]: https://img.shields.io/github/issues/karafra/steg-utility.svg?style=for-the-badge
[issues-url]: https://github.com/karafra/steg-utility/issues
[license-shield]: https://img.shields.io/github/license/karafra/steg-utility.svg?style=for-the-badge
[license-url]: https://github.com/karafra/steg-utility/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[product-screenshot]: images/screenshot.png
[codecov-shield]: https://img.shields.io/codecov/c/gh/karafra/steg-utility/main?style=for-the-badge&token=20T7e2SGUw
[codecov-url]: https://app.codecov.io/gh/karafra/steg-utility/
[pypi-shield]: https://img.shields.io/pypi/wheel/simple-steganography?style=for-the-badge
[pypi-url]: https://pypi.org/project/simple-steganography/
[documentation-generation-shield]: https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fkarafra%2Fsteg-utility%2Fbadge%3Fref%3Dmaster&style=for-the-badge
[documentation-generation-url]: https://github.com/karafra/steg-utility/actions/workflows/continuous-documentation.yml