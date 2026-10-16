# Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance

## B-097a477400225d

https://arxiv.org/html/2510.21590#chars-10412-12007

### 3.1 Architecture Overview

Current image super-resolution methods focus on enhancing overall image quality but often fail to accurately preserve glyph structures, leading to distorted text in super-resolved images, as shown in [Fig. 1](#S0.F1 "In Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") (b).
Conversely, text image super-resolution methods improve text readability but do not retain the global semantic information of the background, causing incoherence between text and non-text regions.
To leverage the strengths of both approaches, we introduce the TiGeSR framework.
As illustrated in [Fig. 2](#S2.F2 "In 2 Related Works ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), the TiGeSR framework is composed of 2 stages, the Text Restoration stage and the Image Enhancement stage.
In the text restoration stage, we extract the text regions from the LR input xL∈ℝH×W×Cx\_{L}\in\mathbb{R}^{H\times W\times C} and feed them into the glyph structure restoration model to restore the text structure based on the text region of the LR input and the predicted text.
We then reassemble the text structures to their original positions to obtain a text mask x^m∈ℝH×W×C\hat{x}\_{m}\in\mathbb{R}^{H\times W\times C}.
In the image enhancement stage, the text mask and LR input are then processed by a ControlNet-like network to obtain the enhanced SR output x^H∈ℝH×W×C\hat{x}\_{H}\in\mathbb{R}^{H\times W\times C}.
The following sections detail each stage.

## B-0a080074d70afa

https://arxiv.org/html/2510.21590#chars-51785-53148

## 13 Alignment Comparison

We compare our proposed Cascade Coarse-to-Fine alignment strategy with the alignment method proposed by RealSR [[2](#bib.bib2)] and single-time alignment using SIFT.
During the comparison, we implement our strategy using SIFT and utilize the raw images from the 35mm dataset of our proposed UZ-ST dataset for evaluation.
For metrics, we adopt PSNR, Mean Squared Error (MSE), SSIM [[42](#bib.bib42)], Normalized Cross-Correlation (NCC), and Average Keypoint Distance (AKD) to assess the alignment quality of the aligned image.

As shown in [Tab. 8](#Sx1.T8 "In Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") and [Fig. 6](#S12.F6 "In 12 More details of UZ-ST ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), pixel-based optimization methods break when handling heavily degraded images due to significant loss of details. Keypoint-based alignment like SIFT suffers from the lack of valid keypoint for matching.
While our alignment method outperforms all other methods and achieves the best results, this is due to the progressive cascade alignment strategy, which breaks the hard alignment process into simpler tasks, facilitating the bridging between images taken under different focal lengths.

## B-1250809203db16

https://arxiv.org/html/2510.21590#chars-54579-56157

## 15 Efficiency Analysis

As shown in [Tab. 9](#Sx1.T9 "In Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), stage 1 is a standard diffusion process that takes multiple steps in inference, the efficiency of our model may be suboptimal compared to one-step methods.
However, our method achieves state-of-the-art performance in OCR-A, which cannot be easily obtained by extending inference time.

![Refer to caption](2510.21590v3/Appendix_qua1_V2.png)
![Refer to caption](2510.21590v3/Appendix_qua2_V2.png)
![Refer to caption](2510.21590v3/multilingual_V2.png)
![Refer to caption](2510.21590v3/Dataset_examples.png)
![[LOGO]](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)

## B-1342559e146b01

https://arxiv.org/html/2510.21590#chars-56157-57496

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
methods listed below:

**Tip:** You can select the relevant text first, to include it in your report.

Our team has already identified [the following issues](https://github.com/arXiv/html_feedback/issues). We appreciate your time reviewing and reporting rendering errors we
may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability
should not be a barrier to accessing research. Thank you for your continued support in championing open access for
all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a [list of packages that need conversion](https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML), and welcome [developer contributions](https://github.com/brucemiller/LaTeXML/issues).

![Simons Foundation](/static/base/1.0.1/images/funders/simons-foundation.png)
![Simons Foundation International](/static/base/1.0.1/images/funders/simons-foundation-international.png)
![Schmidt Sciences](/static/base/1.0.1/images/funders/schmidt-sciences.png)

## B-1cb8b3c8d6647e

https://arxiv.org/html/2510.21590#chars-46997-47848

## 8 Ethics Statement

This work focuses on improving scene text image super-resolution to support beneficial applications such as enhancing accessibility, document restoration, and navigation assistance.
However, we acknowledge potential risks, including misuse in privacy-sensitive contexts (e.g., recovering text from personal or social media images) or unintended deployment in surveillance.
To mitigate such risks, users are encouraged to combine our methods with privacy-preserving techniques such as watermarking or selective inpainting.
Our UZ-ST dataset was collected from public, non-sensitive scenes under ethical guidelines, without including personally identifiable or private information.
We believe the societal benefits of improved text image restoration outweigh potential risks, provided that the technology is applied responsibly.

## B-2fd65f4d8011d3

https://arxiv.org/html/2510.21590#chars-209-327

# Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance

## B-4767256aa74fd6

https://arxiv.org/html/2510.21590#chars-26902-26919

## 5 Experiment

## B-533ded88c7462e

https://arxiv.org/html/2510.21590#chars-16754-19449

### 3.3 Image Enhancement stage

Image Enhancement pipeline. To effectively take advantage of the generated glyph structure x^m\hat{x}\_{m} and enhance the quality of LR xLx\_{L}, we adopt a ControlNet [[56](#bib.bib56)] network ϵϕ\epsilon\_{\phi}.
As illustrated in [Fig. 2](#S2.F2 "In 2 Related Works ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), after getting their latent representation z^m\hat{z}\_{m} and zLz\_{L}, we use the network to denoise the zLz\_{L} only at the specific timestep tt, using the null-text embedding cN​u​l​lc\_{Null}.
The output super-resolved latent representation z^H\hat{z}\_{H} will be denoted as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | z^H=zL−σt​ϵϕ​(zL,z^m,t,cN​u​l​l),\hat{z}\_{H}=z\_{L}-\sigma\_{t}\epsilon\_{\phi}(z\_{L},\hat{z}\_{m},t,c\_{Null}), |  | (4) |

where σt\sigma\_{t} is a scalar determined by the predefined diffusion time step.
With the text restoration stage, this image enhancement pipeline forms a progressive ‘text-first, image after’ paradigm. Our design injects structure-aware control into the generative process, allowing the network to enhance global image quality while preserving text structures.

Training Strategy. For the quality of image super-resolution, we constrain the reconstruction loss between the predicted high-resolution image x^H\hat{x}\_{H} decoded from z^H\hat{z}\_{H} by ε\varepsilon and the ground truth high-resolution image xHx\_{H} using a weighted sum of MSE and LPIPS losses:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒi​m​g=λl​2​‖xH−x^H‖22+λL​P​I​P​S​LPIPS​(xH,x^H),\mathcal{L}\_{img}=\lambda\_{l2}\|x\_{H}-\hat{x}\_{H}\|^{2}\_{2}+\lambda\_{LPIPS}\text{LPIPS}(x\_{H},\hat{x}\_{H}), |  | (5) |

where λl​2\lambda\_{l2} and λL​P​I​P​S\lambda\_{LPIPS} are balancing coefficients for different loss terms.
To enhance glyph control and emphasize the glyph structure, we extract the text boundaries using Sobel operators [[34](#bib.bib34)]. This edge loss is expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒe​d​g​e=‖Sobel​(xH)−Sobel​(x^H)‖22.\mathcal{L}\_{edge}=\|\text{Sobel}(x\_{H})-\text{Sobel}(\hat{x}\_{H})\|^{2}\_{2}. |  | (6) |

We combine the two loss terms and use λe​d​g​e\lambda\_{edge} as the balancing coefficient in the complete loss function for stage 2:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=ℒi​m​g+λe​d​g​e​ℒe​d​g​e.\mathcal{L}=\mathcal{L}\_{img}+\lambda\_{edge}\mathcal{L}\_{edge}. |  | (7) |

The combination of glyph-aware ControlNet conditioning and edge-constrained training objectives enables our model to preserve stroke integrity while harmonizing text and background appearance.

## B-60d3aacd38ab87

https://arxiv.org/html/2510.21590#chars-7324-10394

## 2 Related Works

![Refer to caption](2510.21590v3/PipelineV6.png)

Real-World Image Super-Resolution. 
Real-world image super-resolution (Real-SR) aims to reconstruct high-resolution (HR) images from low-resolution (LR) inputs degraded under uncontrolled real-world conditions.
Early GAN-based methods, such as BSRGAN [[55](#bib.bib55)] and Real-ESRGAN [[44](#bib.bib44)], synthesize degradations through random combinations of known distortions and use adversarial training for restoration.
While they generate natural-looking images, their instability and insensitivity to fine details limit their ability to recover structural elements, especially text.
Recent work introduces diffusion models into Real-SR [[53](#bib.bib53), [45](#bib.bib45)], improving perceptual quality but still struggling with complex structures like scene text.
StableSR [[41](#bib.bib41)] and DiffBIR [[27](#bib.bib27)] apply ControlNet [[56](#bib.bib56)] to condition generation on LR inputs, while PASD [[48](#bib.bib48)] and SeeSR [[47](#bib.bib47)] incorporate high-level semantics to enhance fidelity.
SUPIR [[50](#bib.bib50)] scales training with large image-text pairs and introduces degradation-robust encoders.
Other approaches, including OSEDiff [[46](#bib.bib46)] and TSD-SR [[14](#bib.bib14)], directly apply the diffusion process on LR images and distill models for one-step sampling.
DiT-SR [[6](#bib.bib6)], DreamClear [[1](#bib.bib1)], and DiT4SR [[15](#bib.bib15)] adopt diffusion transformers (DiT) for Real-SR.
Despite enhancing perceptual fidelity, these methods often overlook accurate text structures.
TADiSR [[19](#bib.bib19)] addresses Chinese scene text super-resolution by using Kolors as the base model and aggregating cross-attention maps for text structure supervision.
However, constrained by the resolution of cross-attention, it struggles to restore small or severely degraded text.

Text Image Super-Resolution. Text image super-resolution (Text-SR) restores textual content from cropped images of isolated words or text lines.
Early methods [[12](#bib.bib12)] apply general SR architectures such as SRCNN [[11](#bib.bib11)] to enhance OCR performance.
TextSR [[42](#bib.bib42)] introduces GANs with a recognition loss, while PlugNet [[32](#bib.bib32)] and STT [[4](#bib.bib4)] jointly train SR and recognition modules for more discriminative features.
TSRN [[43](#bib.bib43)] releases the TextZoom dataset and employs an edge-aware module to preserve text details, while TATT [[30](#bib.bib30)] uses global attention for irregular layouts.
Methods like MTDM [[40](#bib.bib40)] inpaint text but fail on complex scripts due to primitive architectures.
MARCONet [[25](#bib.bib25)] employs StyleGAN priors and a glyph structure codebook for realistic text reconstruction.
DiffTSR [[58](#bib.bib58)] employs latent diffusion to separately denoise text and text-image components.
Despite progress in text structure restoration, existing methods lack global background constraints, causing style inconsistencies and block artifacts between text and background.

## B-6658009dafef11

https://arxiv.org/html/2510.21590#chars-51260-51785

## 12 More details of UZ-ST

In [Tab. 7](#Sx1.T7 "In Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), we provide detailed statistics on the composition of the UZ-ST dataset.
Additionally, in [Fig. 10](#S15.F10 "In 15 Efficiency Analysis ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), we present some example images from the dataset.

![Refer to caption](2510.21590v3/Alignment.png)

## B-69bcc27f3edca2

https://arxiv.org/html/2510.21590#chars-10394-10412

## 3 Methodology

## B-84f84aaca5f211

https://arxiv.org/html/2510.21590#chars-48049-48632

## 10 Dataset Collection

We use VIVO X200 Ultra to collect images for 4 separate focal lengths (14 mm, 35 mm, 84 mm, and 200 mm).
We first use PP-OCRV5 [[7](#bib.bib7)] for the rough annotation, then we manually filter the images and annotations.
During the filtering and annotation, each image undergoes the following rules:

Width or height of the image should be no less than 256.

Height of the text should not be less than 32 pixels.

Score of OCR recognition of the text should not be lower than 0.9.

Content of the text should not be empty or consist solely of whitespace.

## B-89314628f51797

https://arxiv.org/html/2510.21590#chars-27851-30414

#### 5.2.1 Quantitative Results

We evaluate existing competing methods, including GAN-based image super-resolution approaches such as Real-ESRGAN [[44](#bib.bib44)] and HAT [[5](#bib.bib5)]; diffusion-based approaches such as SeeSR [[47](#bib.bib47)], SupIR [[50](#bib.bib50)], DiffBIR [[27](#bib.bib27)], OSEDiff [[46](#bib.bib46)], DreamClear [[1](#bib.bib1)], TSD-SR [[14](#bib.bib14)], and DiT4SR [[15](#bib.bib15)]; as well as text-focused reconstruction methods such as MARCONet [[25](#bib.bib25)], DiffTSR [[58](#bib.bib58)], and TADiSR [[19](#bib.bib19)].
Evaluations are performed on the Real-CE Benchmark [[31](#bib.bib31)] and the benchmark described in [Sec. 4](#S4 "4 Dataset and Benchmark ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance").
To ensure fairness, we fine-tune the released pre-trained models on the training sets of both benchmarks using the official code when available.
Following [[19](#bib.bib19)], we integrate the outputs of MARCONet and DiffTSR with HAT-generated results to simulate real-world application scenarios and enable comprehensive full-image evaluation.
We evaluate Real-CE at the hardest difficulty level (×4\times 4), while UZ-ST is evaluated across all difficulty levels—with average results reported here.
Detailed per-level evaluations appear in the [Sec. 14](#S14 "14 Additional results ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance").

As shown in [Tab. 2](#S4.T2 "In 4 Dataset and Benchmark ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") and [Tab. 3](#S4.T3 "In 4 Dataset and Benchmark ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance")
, TiGeSR outperforms competing methods on both the Real-CE and UZ-ST benchmarks in terms of image quality and text accuracy.
TADiSR, limited by the resolution of its cross-attention mechanism, performs poorly under severe degradation and with small text.
DiffTSR and MARCONet fail to effectively handle text backgrounds and struggle with text regions that have a large width-to-height aspect ratio.
In contrast, our method restores images with high quality and fine-grained text, owing to the decoupling strategy.
It achieves OCR-A scores above 0.67 and 0.43, and demonstrates overall superiority in both pixel-level and perceptual accuracy.

![Refer to caption](2510.21590v3/ablationV7.png)

## B-8fde0bdf20ef2c

https://arxiv.org/html/2510.21590#chars-19449-26902

## 4 Dataset and Benchmark

Existing datasets like [Ma et al. [31]](#bib.bib31) offer only subtle degradation, as shown in [Fig. 3](#S3.F3 "In 3.2 Text Restoration stage ‣ 3 Methodology ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") (a), making them insufficient for evaluating model robustness.
To address the lack of both challenging and publicly available datasets tailored for scene text image super-resolution, especially for Chinese text, we introduce UZ-ST, a challenging real-world benchmark.
It is collected using ViVO X200 Ultra equipped with four fixed focal lengths (14 mm, 35 mm, 85 mm, 200 mm), enabling image pairs with a maximum zoom of ×14.29\times 14.29.
It includes diverse scenes—street views, book covers, advertisements, menus, and posters—captured under varied lighting, with all text lines manually annotated.
However, such zoom introduces severe misalignment that breaks pixel-wise optimization methods like [[2](#bib.bib2)], originally designed for moderate ×2\times 2 to ×4\times 4 zoom.
To address this, we design a Cascade Coarse-to-fine Alignment pipeline (see [Fig. 3](#S3.F3 "In 3.2 Text Restoration stage ‣ 3 Methodology ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") (b)): images are first sorted by focal length, and each low-quality image is sequentially aligned to its next higher-focal neighbor using optimization-based registration or feature-based extractors [[29](#bib.bib29), [22](#bib.bib22)], then refined against the 200 mm ground truth.
Finally, we manually filter or realign problematic cases to ensure precise alignment.

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Methods | Real-CE | | | | | | UZ-ST | | | | | |
| PSNR↑\uparrow | SSIM↑\uparrow | LPIPS↓\downarrow | DISTS↓\downarrow | FID↓\downarrow | OCR-A ↑\uparrow | PSNR↑\uparrow | SSIM↑\uparrow | LPIPS↓\downarrow | DISTS↓\downarrow | FID↓\downarrow | OCR-A ↑\uparrow |
| Real-ESRGAN | 22.30 | 0.787 | 0.239 | 0.188 | 53.60 | 56.0% | 23.99 | 0.790 | 0.248 | 0.194 | 30.60 | 37.1% |
| HAT | 23.61 | 0.830 | 0.214 | 0.176 | 51.16 | 56.6% | 25.17 | 0.815 | 0.249 | 0.198 | 30.12 | 37.9% |
| MARCONet | 21.89 | 0.785 | 0.238 | 0.150 | 52.97 | 55.0% | 22.13 | 0.768 | 0.306 | 0.205 | 34.28 | 33.4% |
| SeeSR | 23.59 | 0.822 | 0.195 | 0.169 | 43.75 | 37.4% | 23.64 | 0.788 | 0.219 | 0.184 | 26.73 | 22.8% |
| SupIR | 21.78 | 0.723 | 0.310 | 0.198 | 44.94 | 27.8% | 23.62 | 0.754 | 0.308 | 0.207 | 27.91 | 23.6% |
| DiffTSR | 22.10 | 0.768 | 0.278 | 0.168 | 44.91 | 44.1% | 22.41 | 0.767 | 0.300 | 0.189 | 31.25 | 31.7% |
| DiffBIR | 22.44 | 0.747 | 0.260 | 0.201 | 46.44 | 37.6% | 23.67 | 0.724 | 0.262 | 0.197 | 23.10 | 26.6% |
| OSEDiff | 21.86 | 0.771 | 0.197 | 0.127 | 41.00 | 26.8% | 25.07 | 0.819 | 0.201 | 0.169 | 20.53 | 28.9% |
| DreamClear | 22.47 | 0.772 | 0.216 | 0.157 | 38.97 | 50.2% | 24.10 | 0.773 | 0.238 | 0.191 | 21.75 | 21.4% |
| TSD-SR | 21.43 | 0.754 | 0.220 | 0.175 | 47.21 | 34.9% | 22.79 | 0.757 | 0.207 | 0.194 | 24.08 | 26.6% |
| DiT4SR | 20.54 | 0.764 | 0.268 | 0.186 | 49.79 | 29.2% | 23.16 | 0.767 | 0.215 | 0.159 | 20.58 | 23.7% |
| TADiSR | 23.83 | 0.790 | 0.286 | 0.154 | 44.42 | 64.7% | 24.61 | 0.796 | 0.203 | 0.160 | 36.61 | 36.6% |
| TiGeSR (Ours) | 24.12 | 0.839 | 0.164 | 0.125 | 38.72 | 67.3% | 25.48 | 0.830 | 0.196 | 0.156 | 20.01 | 43.0% |

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Methods | Real-CE | | | | | UZ-ST | | | | |
| PSNRcr↑\uparrow | SSIMcr ↑\uparrow | LPIPScr ↓\downarrow | DISTScr ↓\downarrow | Δ\Delta OCR-A ↑\uparrow | PSNRcr ↑\uparrow | SSIMcr ↑\uparrow | LPIPScr ↓\downarrow | DISTScr ↓\downarrow | Δ\Delta OCR-A ↑\uparrow |
| Real-ESRGAN | 21.71 | 0.824 | 0.257 | 0.224 | -8.8% | 21.25 | 0.786 | 0.302 | 0.266 | -4.7% |
| HAT | 23.03 | 0.862 | 0.249 | 0.239 | -8.2% | 22.18 | 0.813 | 0.291 | 0.276 | -3.9% |
| MARCONet | 20.68 | 0.786 | 0.267 | 0.223 | -9.8% | 17.48 | 0.690 | 0.529 | 0.366 | -8.3% |
| SeeSR | 22.74 | 0.844 | 0.237 | 0.212 | -27.4% | 20.45 | 0.767 | 0.297 | 0.241 | -18.9% |
| SupIR | 19.96 | 0.778 | 0.326 | 0.263 | -37.0% | 20.10 | 0.756 | 0.344 | 0.287 | -18.2% |
| DiffTSR | 20.46 | 0.818 | 0.275 | 0.239 | -20.7% | 17.00 | 0.665 | 0.452 | 0.313 | -10.0% |
| DiffBIR | 21.20 | 0.792 | 0.278 | 0.224 | -27.2% | 20.70 | 0.757 | 0.302 | 0.245 | -15.2% |
| OSEDiff | 19.38 | 0.768 | 0.269 | 0.208 | -38.0% | 21.43 | 0.798 | 0.276 | 0.263 | -12.8% |
| DreamClear | 22.74 | 0.845 | 0.190 | 0.168 | -14.6% | 20.50 | 0.768 | 0.317 | 0.276 | -20.3% |
| TSD-SR | 19.33 | 0.763 | 0.279 | 0.234 | -29.9% | 19.42 | 0.748 | 0.296 | 0.249 | -15.1% |
| DiT4SR | 17.95 | 0.738 | 0.317 | 0.244 | -35.6% | 19.73 | 0.760 | 0.273 | 0.216 | -18.0% |
| TADiSR | 23.39 | 0.855 | 0.253 | 0.258 | -1.0% | 21.59 | 0.799 | 0.360 | 0.336 | -5.1% |
| TiGeSR (Ours) | 23.43 | 0.864 | 0.173 | 0.167 | +2.5% | 22.22 | 0.814 | 0.228 | 0.212 | +1.3% |

Through meticulous annotation and alignment, we obtained 5,036 image pairs with 49,675 text lines.
We treat images captured under 200 mm focal lengths as GT, yielding 1,439, 1,798, and 1,799 pairs for the ×14.29\times 14.29, ×5.71\times 5.71, and ×2.35\times 2.35 zoom modes, respectively.
Among them, we randomly select 470, 589, and 581 pairs for evaluation under each zoom mode.
Each image pair contains one or more text lines.
These evaluation sets allow us to assess model performance in more complex and challenging scenarios.

For the UZ-ST-benchmark, we utilize 5 evaluation metrics to examine the quality of image super-resolution on the scale of the full image.
Firstly, we adopt Peak Signal-to-Noise Ratio (PSNR), Structural Similarity Index Measure (SSIM) [[42](#bib.bib42)], Learned Perceptual Image Patch Similarity (LPIPS) [[57](#bib.bib57)], Deep Image Structure and Texture Similarity (DISTS) [[10](#bib.bib10)], and Fréchet Inception Distance (FID) [[17](#bib.bib17)] for evaluation of image quality.
Specifically, PSNR and SSIM are computed in the pixel space to quantify low-level reconstruction fidelity, LPIPS and DISTS are computed in the feature space to assess perceptual similarity, and FID is employed to evaluate the distributional discrepancy between generated and real images.
However, these metrics do not directly reflect the quality or accuracy of super-resolved text. To address this, we crop annotated text regions from the images and compute PSNR, SSIM, LPIPS, and DISTS on these cropped regions, denoted as PSNR​c​r\text{PSNR}{cr}, SSIM​c​r\text{SSIM}{cr}, LPIPS​c​r\text{LPIPS}{cr}, and DISTS​c​r\text{DISTS}{cr}.
For text accuracy, we apply an OCR model to recognize the text and compare its outputs with the ground-truth annotations using the Levenshtein ratio [[54](#bib.bib54)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | OCR-A=Len​(sp​r​e​d)+Len​(sg​t)−Dist​(sp​r​e​d,sg​t)Len​(sp​r​e​d)+Len​(sg​t),\displaystyle\text{OCR-A}=\frac{\text{Len}(s\_{pred})+\text{Len}(s\_{gt})-\text{Dist}(s\_{pred},s\_{gt})}{\text{Len}(s\_{pred})+\text{Len}(s\_{gt})}, |  | (8) |

where sp​r​e​ds\_{pred} stands for the predicted text sequence, sg​ts\_{gt} denotes annotated ground-truth text sequence, and Dist​(⋅,⋅)\text{Dist}(\cdot,\cdot) is the Levenshtein distance between text sequences.

![Refer to caption](2510.21590v3/quaV4.png)

## B-98f0be01bf0f58

https://arxiv.org/html/2510.21590#chars-38685-39115

## Acknowledgement

This work was supported by the NSFC under Grant Nos. 62361166670, U24A20330, Shenzhen Science and Technology Program (JCYJ20240813114237048), “Science and Technology Yongjiang 2035” key technology breakthrough plan project (2024Z120), Chinese government-guided local science and technology development fund projects (scientific and technological achievement transfer and transformation projects) (254Z0102G).

## B-9cf246deb53618

https://arxiv.org/html/2510.21590#chars-26919-27823

### 5.1 Implementation Details

We combine synthetic data (built upon LSDIR [[26](#bib.bib26)] with text rendered via LBTS [[38](#bib.bib38)] and Real-ESRGAN [[44](#bib.bib44)] degradation) and real data from Real-CE [[31](#bib.bib31)] and UZ-ST. Misaligned pairs in Real-CE are filtered and reannotated, yielding 337 training and 188 testing pairs. Stage 1 uses cropped text regions and is trained using an IDM-based architecture [[58](#bib.bib58)] with combined segmentation and reconstruction losses. Stage 2 is based on Stable Diffusion 3.5 [[16](#bib.bib16)] and employs a tile-based inference strategy [[50](#bib.bib50), [19](#bib.bib19)]; it is pretrained on synthetic data and fine-tuned on real data. For more details, see the [Sec. 11](#S11 "11 More Implementation Details ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance").

## B-a6295ea22c5fac

https://arxiv.org/html/2510.21590#chars-45958-46997

## 7 Reproducibility Statement

To ensure reproducibility, we have made the following efforts:

We will release our code and dataset.

We provide implementation details in [Sec. 5.1](#S5.SS1 "5.1 Implementation Details ‣ 5 Experiment ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") and [Sec. 11](#S11 "11 More Implementation Details ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), including the training process and selection of hyper-parameters.

We provide details on evaluation metrics and dataset preparation in [Sec. 4](#S4 "4 Dataset and Benchmark ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") and [Sec. 10](#S10 "10 Dataset Collection ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), and the code and data will be made available along with it.

## B-ad6c881dc94034

https://arxiv.org/html/2510.21590#chars-1246-7324

## 1 Introduction

Scene Text Image Super-Resolution is a critical problem in computer vision for its vital role in downstream applications [[24](#bib.bib24), [20](#bib.bib20), [8](#bib.bib8), [37](#bib.bib37)].
It seeks to restore a high-quality super-resolution (SR) image from a degraded low-resolution (LR) input while preserving the text meaning.
Unlike general image super-resolution for natural scenes, where plausible texture synthesis or detail hallucination is acceptable and does not alter the semantic meaning of the image, visual texts exhibit extremely low tolerance to structural errors.
This is especially evident in Chinese, where a minor stroke distortion or omission may entirely alter the meaning [[52](#bib.bib52), [25](#bib.bib25)].

In recent years, with the rapid development of generative models such as diffusion [[18](#bib.bib18), [9](#bib.bib9), [36](#bib.bib36), [33](#bib.bib33), [35](#bib.bib35), [3](#bib.bib3), [59](#bib.bib59)], image super-resolution has increasingly relied on their strong generative priors to recover missing details from low-resolution (LR) inputs [[47](#bib.bib47), [50](#bib.bib50), [27](#bib.bib27), [46](#bib.bib46), [13](#bib.bib13), [15](#bib.bib15), [19](#bib.bib19)].
Although these approaches can effectively restore fine-grained natural textures (*e.g*., grass, leaves), they often distort text regions, turning them into gibberish as shown in Fig.[1](#S0.F1 "Figure 1 ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") (b).
Because their primary goal is overall image enhancement, they tend to overlook text structure, resulting in a limited ability to preserve fine-grained glyph details.
This limitation is amplified for Chinese characters, due to their complex and diverse glyph designs and relatively low saliency in images.
Consequently, models tend to under-represent and collapse glyphs into oversimplified, averaged forms, producing overlapping or distorted characters.
Some researchers attempt to address this by processing only text regions [[58](#bib.bib58), [25](#bib.bib25)].
While these methods improve readability notably, the absence of global background constraints often introduces style inconsistencies and block artifacts between text and background.
Ultimately, current approaches face a persistent trade-off between maintaining readability and ensuring high image quality.
Our key observation is that these goals need not be mutually exclusive if text and non-text are explicitly handled differently.
Text structures can be reconstructed with dedicated mechanisms and then used to guide full-image restoration, ensuring coherent style without artifacts.

Building on this insight, we introduce TiGeSR (Text–image Guided Super-Resolution), a progressive two-stage paradigm for scene text super-resolution built on the principle of “restoring text structure first, enhancing the whole image later.” 
Unlike methods that rely on a single generative prior, TiGeSR explicitly separates the treatment of text and non-text regions: a diffusion-based local text refiner focuses on reconstructing fine-grained stroke geometry in text regions, ensuring glyph fidelity and structural consistency.
The recovered text structures are then injected as conditional guidance into the subsequent full-image restoration stage, steering global super-resolution to harmonize text and background while suppressing artifacts and preserving overall visual quality.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Content | TextZoom | CTR | Real-CE | UZ-ST (Ours) |
| Chinese characters | ✗ | ✓ | ✓ | ✓ |
| Multi-line text | ✗ | ✗ | ✓ | ✓ |
| Real-World Degradation(>×4>\!\times 4) | ✗ | ✗ | ✗ | ✓ |

Moreover, existing scene text super-resolution datasets [[43](#bib.bib43), [51](#bib.bib51), [31](#bib.bib31)] are limited to mild degradation (≤×4\leq\!\times 4), which fails to reflect real-world long-distance scenarios and restricts models from learning robust low- to high-resolution mappings.
To address the issue of data scarcity and enable comprehensive evaluation [[43](#bib.bib43), [31](#bib.bib31)], we introduce the UZ-ST (UltraZoom-Sence Text) benchmark dataset, the first scene text dataset that contains a maximum zooming mode of ×14.29\times 14.29, providing extra challenging scenarios for the field.
Content differences are outlined in [Tab. 1](#S1.T1 "In 1 Introduction ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance").
It includes high-quality 5,036 LR–HR pairs captured at multiple focal lengths (ranging from 14mm to 200mm), with 49,675 text lines in total.
Each pair comes with detailed annotations, including detection boxes and text transcripts, to support both training and evaluation.
The dataset includes diverse scenarios such as shop signs, posters, and documents.
It also covers varying lighting conditions, including daylight, indoor lighting, and nighttime, offering a challenging yet practical benchmark for the field.
To ensure reliable alignment across focal lengths, we adopt a coarse-to-fine cascade alignment strategy combined with manual filtering: coarse alignment is performed via global geometric transformation, and residual misalignments are corrected through local refinement.
This process achieves accurate LR–HR alignment, thereby ensuring both the quality of the dataset and the reliability of our experiments. The main contributions are summarized as follows:

We propose TiGeSR, the first two-stage scene text super-resolution framework with a ‘text-first, image-later’ paradigm that decouples glyph restoration from image enhancement, improving readability and visual quality.

We introduce UZ-ST, the first scene text benchmark with maximum zoom of ×\times14.29, offering aligned, richly annotated LR–HR pairs for thorough evaluation under challenging real-world conditions.

Extensive experiments on Real-CE and UZ-ST show our method outperforms prior state-of-the-art models, especially in preserving text structure.

## B-c0469d94bb6948

https://arxiv.org/html/2510.21590#chars-327-1246

###### Abstract

Current image super-resolution methods show strong performance on natural images but distort text, creating a fundamental trade-off between image quality and textual readability.
To address this, we introduce TiGeSR (Text–image Guided Super-Resolution), a two-stage framework that breaks this trade-off through a “text-first, image-later” paradigm.
TiGeSR explicitly decouples glyph restoration from image enhancement: it first reconstructs precise text structures and uses them to guide full-image super-resolution.
This ensures high fidelity and readability.
For comprehensive training and evaluation, we present the UZ-ST (UltraZoom-Scene Text) dataset, the first Chinese scene text dataset with highest zoom of ×14.29\times 14.29.
Extensive experiments show TiGeSR achieves state-of-the-art performance, enhancing readability and image quality.

![[Uncaptioned image]](2510.21590v3/TeaserV10.png)

## B-c16f602a1019ef

https://arxiv.org/html/2510.21590#chars-48632-51260

## 11 More Implementation Details

Dataset Settings. For training, we combine a synthetic dataset with real paired datasets (Real-CE [[31](#bib.bib31)] and UZ-ST).
Our synthetic dataset builds upon LSDIR [[26](#bib.bib26)], containing 27,000 triplets (xH,xL,xm)(x\_{H},x\_{L},x\_{m}).
We render text on the GT of LSDIR and the corresponding text mask using the LBTS [[38](#bib.bib38)], then apply Real-ESRGAN degradation [Wang et al. [44]](#bib.bib44) to generate LR images.
Since there are misaligned image pairs in Real-CE [[19](#bib.bib19), [58](#bib.bib58)] and text lines not annotated, we filter out misaligned image pairs and reannotate the images manually.
In the end, we obtain 337 training pairs and 188 testing pairs from the Real-CE dataset.
Images under 13mm and 52mm focal lengths are considered as LR xLx\_{L} and GT xHx\_{H}, respectively.
Following [Hu et al. [19]](#bib.bib19), we use SAM-TS [[49](#bib.bib49)] to obtain the text mask xmx\_{m} from xHx\_{H}.
UZ-ST triplets (xH,xL,xm)(x\_{H},x\_{L},x\_{m}) are processed identically.
For stage 1 training, we use cropped text regions from the dataset, while for stage 2, we use full images.
Following [[39](#bib.bib39)], we use PP-OCRv3 [[23](#bib.bib23)] to extract strings from the text region of predicted SR for evaluation of OCR-A.

Training Details. For stage 1, we build our model based on the IDM baseline of DiffTSR [[58](#bib.bib58)].
We set λt​d\lambda\_{td}, λS​e​g\lambda\_{Seg}, λF​o​c​a​l\lambda\_{Focal}, and λD​i​c​e\lambda\_{Dice} as 11, 0.10.1, 2020, and 11 respectively.
In stage 2, our model is built upon Stable Diffusion 3.5 medium [[16](#bib.bib16)] and follows a similar tile-based inference strategy to TADiSR [[19](#bib.bib19)] and SUPIR [[50](#bib.bib50)].
The timestep tt is set to 150150.
The conditioning scale of the ControlNet is set to 1.0.
λl​2\lambda\_{l2}, λL​P​I​P​S\lambda\_{LPIPS}, and λe​d​g​e\lambda\_{edge} are set to 11, 55, 100100 when using the synthetic dataset for pretraining.
Then, λe​d​g​e\lambda\_{edge} is set to 00 and the remaining coefficients are kept unchanged when training on real paired datasets.
We train both stages of the model using the AdamW [[28](#bib.bib28)] optimizer and set the learning rate to 5×10−55\times 10^{-5} and 5×10−65\times 10^{-6} for stages 1 and 2 separately.
All experiments are conducted on NVIDIA H20 GPUs.
For stage 1, we train the model on synthetic and real datasets for 8 epochs, then finetune it on synthetic data for 2 epochs.
For stage 2, we first pretrain the model on the synthetic dataset for 50 epochs.
Then we train on the real paired datasets for 50 epochs.

## B-c7ef5909a840ea

https://arxiv.org/html/2510.21590#chars-30414-32005

#### 5.2.2 Qualitative Results

[Fig. 4](#S4.F4 "In 4 Dataset and Benchmark ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") shows visual comparisons on Real-CE and UZ-ST.
Real-world degradations cause noise, blurred strokes, and distortions in the input images.
GAN-based methods reduce noise but fail to fix text structure, while diffusion-based SR methods, though powerful, lack text-structure guidance and often distort strokes, sometimes making text unreadable.

Methods tailored for text image super resolution (e.g., MARCONet and DiffTSR) exhibit limitations in processing long text sequences, often generating distorted or semantically meaningless results.
They also lack global semantic guidance, making it hard to blend text regions with backgrounds.
As seen in [Fig. 4](#S4.F4 "In 4 Dataset and Benchmark ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") (a), DiffTSR+HAT (red box) produces text colors inconsistent with the original LR and SR output of HAT.
In [Fig. 4](#S4.F4 "In 4 Dataset and Benchmark ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") (b), it even distorts the face near the word “Ory”.
TADiSR works well on lightly degraded images but fails under severe degradation and performs poorly on small text due to cross-attention mask resolution limits.
Our method overcomes these issues, restoring high-quality glyph structures even in challenging cases.

## B-cd04a64bc4f144

https://arxiv.org/html/2510.21590#chars-39115-45958

## References

Supplementary Material

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Subset | image count | line count | mean lines/img | img >> 5 lines |
| 14 mm | 1,439 | 15,073 | 10.47 | 754 |
| 35 mm | 1,798 | 17,263 | 9.60 | 867 |
| 85 mm | 1,799 | 17,339 | 9.64 | 869 |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Alignment Method | PSNR ↑\uparrow | MSE ↓\downarrow | SSIM ↑\uparrow | NCC ↑\uparrow | AKD ↓\downarrow |
| RealSR | 13.87 | 4002.65 | 0.5072 | 0.3285 | 546.78 |
| SIFT Alignment (Single time) | 12.77 | 6332.79 | 0.4896 | 0.4313 | 546.78 |
| Cascade Coarse-to-Fine Alignment (Ours) | 23.00 | 441.52 | 0.7279 | 0.9184 | 241.44 |

|  |  |  |  |
| --- | --- | --- | --- |
| Methods | Flops (GFLOPs) | Speed (ms) | OCR-A |
| HAT | 6670.32 | 1086.68 | 37.9% |
| DiffTSR | 58502.14 | 8610.59 | 31.7% |
| DiT4SR w/o llava | 160787.14 | 17385.14 | 23.7% |
| DreamClear w/o llava | 412843.67 | 83193.81 | 21.4% |
| TADiSR | 4497.96 | 342.32 | 36.6% |
| TiGeSR (ours) Stage 1 | 6215.85 | 663.5 | 43.0% |
| TiGeSR (ours) Stage 2 | 3734.01 | 360.06 |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Methods | PSNR↑\uparrow | SSIM↑\uparrow | LPIPS↓\downarrow | DISTS↓\downarrow | FID↓\downarrow | OCR-A↑\uparrow |
| TADiSR | 24.68 | 0.795 | 0.362 | 0.227 | 52.13 | 35.5% |
| TiGeSR (Ours) performance under different randomness of OCR output. | | | | | | |
| 100% Random Text | 25.60 | 0.833 | 0.188 | 0.150 | 28.92 | 40.3% |
| 50% Random Text | 25.60 | 0.833 | 0.189 | 0.151 | 28.92 | 40.6% |
| 20% Random Text | 25.63 | 0.834 | 0.185 | 0.150 | 29.3 | 43.7% |
| 0% Random Text (Ours) | 25.63 | 0.834 | 0.185 | 0.150 | 28.82 | 44.6% |

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Methods | PSNR↑\uparrow | SSIM↑\uparrow | LPIPS↓\downarrow | DISTS↓\downarrow | FID↓\downarrow | PSNRcr↑\uparrow | SSIMcr↑\uparrow | LPIPScr↓\downarrow | DISTScr↓\downarrow | OCR-A↑\uparrow |
| 85mm (×2.35\times 2.35) | Real-ESRGAN | 25.84 | 0.854 | 0.139 | 0.130 | 28.25 | 23.59 | 0.843 | 0.170 | 0.168 | 60.8% |
| HAT | 27.33 | 0.873 | 0.128 | 0.133 | 27.21 | 24.76 | 0.870 | 0.139 | 0.146 | 62.0% |
| MACRONet | 22.90 | 0.804 | 0.234 | 0.173 | 40.19 | 17.92 | 0.693 | 0.515 | 0.360 | 54.2% |
| SeeSR | 25.02 | 0.826 | 0.167 | 0.159 | 32.31 | 21.62 | 0.796 | 0.245 | 0.207 | 28.2% |
| SupIR | 25.58 | 0.823 | 0.202 | 0.160 | 29.33 | 21.91 | 0.808 | 0.239 | 0.214 | 33.3% |
| DiffTSR | 23.48 | 0.805 | 0.230 | 0.157 | 35.77 | 17.92 | 0.688 | 0.392 | 0.285 | 48.2% |
| DiffBIR | 25.25 | 0.793 | 0.175 | 0.152 | 24.57 | 22.26 | 0.803 | 0.218 | 0.190 | 36.8% |
| OSEDiff | 26.38 | 0.852 | 0.153 | 0.137 | 23.92 | 22.84 | 0.833 | 0.200 | 0.204 | 41.0% |
| DreamClear | 25.31 | 0.811 | 0.169 | 0.151 | 24.19 | 21.44 | 0.790 | 0.253 | 0.221 | 26.8% |
| TSD-SR | 23.99 | 0.800 | 0.161 | 0.165 | 30.40 | 20.62 | 0.786 | 0.232 | 0.218 | 37.8% |
| DiT4SR | 24.71 | 0.810 | 0.173 | 0.143 | 29.15 | 21.25 | 0.800 | 0.221 | 0.193 | 48.2% |
| TADiSR | 26.31 | 0.858 | 0.177 | 0.149 | 30.47 | 23.55 | 0.856 | 0.175 | 0.178 | 55.7% |
| Ours | 27.00 | 0.871 | 0.123 | 0.120 | 22.34 | 24.31 | 0.860 | 0.135 | 0.142 | 63.2% |
| 35mm (×5.71\times 5.71) | Real-ESRGAN | 23.70 | 0.785 | 0.218 | 0.184 | 42.62 | 20.86 | 0.782 | 0.272 | 0.235 | 34.1% |
| HAT | 25.05 | 0.819 | 0.207 | 0.182 | 41.32 | 21.98 | 0.816 | 0.250 | 0.241 | 34.6% |
| MACRONet | 22.28 | 0.774 | 0.284 | 0.199 | 49.14 | 17.43 | 0.694 | 0.523 | 0.361 | 31.5% |
| SeeSR | 23.76 | 0.795 | 0.198 | 0.175 | 37.92 | 20.55 | 0.778 | 0.271 | 0.222 | 25.2% |
| SupIR | 23.49 | 0.746 | 0.302 | 0.204 | 41.80 | 20.00 | 0.757 | 0.335 | 0.282 | 24.0% |
| DiffTSR | 22.57 | 0.773 | 0.281 | 0.184 | 45.78 | 16.99 | 0.671 | 0.443 | 0.312 | 31.2% |
| DiffBIR | 23.76 | 0.731 | 0.245 | 0.196 | 35.99 | 20.82 | 0.770 | 0.275 | 0.234 | 28.6% |
| OSEDiff | 25.35 | 0.827 | 0.192 | 0.166 | 29.06 | 21.62 | 0.809 | 0.263 | 0.263 | 29.9% |
| DreamClear | 24.20 | 0.778 | 0.209 | 0.177 | 32.08 | 20.66 | 0.779 | 0.283 | 0.251 | 23.9% |
| TSD-SR | 22.93 | 0.757 | 0.200 | 0.199 | 37.61 | 19.64 | 0.760 | 0.282 | 0.246 | 27.3% |
| DiT4SR | 23.45 | 0.774 | 0.204 | 0.158 | 31.73 | 20.12 | 0.779 | 0.250 | 0.208 | 26.5% |
| TADiSR | 24.68 | 0.795 | 0.362 | 0.227 | 52.13 | 21.57 | 0.798 | 0.366 | 0.347 | 35.5% |
| Ours | 25.63 | 0.834 | 0.185 | 0.150 | 28.82 | 22.14 | 0.823 | 0.204 | 0.194 | 44.6% |
| 14mm (×14.29\times 14.29) | Real-ESRGAN | 22.09 | 0.718 | 0.423 | 0.284 | 89.22 | 18.87 | 0.721 | 0.503 | 0.427 | 11.5% |
| HAT | 22.66 | 0.738 | 0.451 | 0.299 | 89.58 | 19.27 | 0.738 | 0.533 | 0.484 | 12.2% |
| MACRONet | 21.00 | 0.716 | 0.422 | 0.254 | 79.67 | 17.01 | 0.680 | 0.553 | 0.382 | 10.1% |
| SeeSR | 21.79 | 0.731 | 0.310 | 0.228 | 64.31 | 18.87 | 0.717 | 0.396 | 0.308 | 13.2% |
| SupIR | 21.38 | 0.681 | 0.447 | 0.268 | 70.09 | 17.99 | 0.690 | 0.487 | 0.383 | 11.0% |
| DiffTSR | 20.88 | 0.713 | 0.412 | 0.233 | 74.07 | 15.87 | 0.630 | 0.538 | 0.348 | 12.0% |
| DiffBIR | 21.61 | 0.630 | 0.392 | 0.255 | 69.64 | 18.61 | 0.685 | 0.438 | 0.328 | 11.3% |
| OSEDiff | 23.11 | 0.768 | 0.274 | 0.214 | 49.76 | 19.44 | 0.740 | 0.385 | 0.334 | 12.7% |
| DreamClear | 22.45 | 0.719 | 0.364 | 0.260 | 62.95 | 19.14 | 0.725 | 0.440 | 0.377 | 11.7% |
| TSD-SR | 21.14 | 0.705 | 0.273 | 0.225 | 57.07 | 17.67 | 0.686 | 0.393 | 0.293 | 11.9% |
| DiT4SR | 20.88 | 0.707 | 0.282 | 0.181 | 47.45 | 17.36 | 0.687 | 0.367 | 0.253 | 11.7% |
| TADiSR | 22.43 | 0.721 | 0.555 | 0.320 | 98.44 | 19.20 | 0.730 | 0.585 | 0.518 | 14.4% |
| Ours | 23.41 | 0.774 | 0.301 | 0.209 | 54.74 | 19.73 | 0.748 | 0.374 | 0.322 | 16.0% |
| Total | RealEsrGAN | 23.99 | 0.790 | 0.248 | 0.194 | 30.60 | 21.25 | 0.786 | 0.302 | 0.266 | 37.1% |
| HAT | 25.17 | 0.815 | 0.249 | 0.198 | 30.12 | 22.18 | 0.813 | 0.291 | 0.276 | 37.9% |
| MARCONet | 22.13 | 0.768 | 0.306 | 0.205 | 34.28 | 17.48 | 0.690 | 0.529 | 0.366 | 33.4% |
| SeeSR | 23.64 | 0.788 | 0.219 | 0.184 | 26.73 | 20.45 | 0.767 | 0.297 | 0.241 | 22.8% |
| SupIR | 23.62 | 0.754 | 0.308 | 0.207 | 27.91 | 20.10 | 0.756 | 0.344 | 0.287 | 23.6% |
| DiffTSR | 22.41 | 0.767 | 0.300 | 0.189 | 31.25 | 17.00 | 0.665 | 0.452 | 0.313 | 31.7% |
| DiffBIR | 23.67 | 0.724 | 0.262 | 0.197 | 23.10 | 20.70 | 0.757 | 0.302 | 0.245 | 26.6% |
| OSEDiff | 25.07 | 0.819 | 0.201 | 0.169 | 20.53 | 21.43 | 0.798 | 0.276 | 0.263 | 28.9% |
| DreamClear | 24.10 | 0.773 | 0.238 | 0.191 | 21.75 | 20.50 | 0.768 | 0.317 | 0.276 | 21.4% |
| TSD-SR | 22.79 | 0.757 | 0.207 | 0.194 | 24.08 | 19.42 | 0.748 | 0.296 | 0.249 | 26.6% |
| DiT4SR | 23.16 | 0.767 | 0.215 | 0.159 | 20.58 | 19.73 | 0.760 | 0.273 | 0.216 | 23.7% |
| TADiSR | 24.61 | 0.796 | 0.203 | 0.160 | 36.61 | 21.59 | 0.799 | 0.360 | 0.336 | 36.6% |
| Ours | 25.48 | 0.830 | 0.196 | 0.156 | 20.01 | 22.22 | 0.814 | 0.228 | 0.212 | 43.0% |

## B-d29ab066c0aa6a

https://arxiv.org/html/2510.21590#chars-32005-37735

### 5.3 Ablation Study

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Methods | PSNR↑\uparrow | SSIM↑\uparrow | LPIPS↓\downarrow | DISTS↓\downarrow | FID↓\downarrow | OCR-A↑\uparrow |
| OSEDiff w/o UZ-ST | 23.50 | 0.791 | 0.197 | 0.162 | 24.30 | 22.8% |
| OSEDiff w/   UZ-ST | 25.07 | 0.819 | 0.201 | 0.169 | 20.53 | 28.9% |
| DiT4SR w/o UZ-ST | 22.58 | 0.754 | 0.252 | 0.196 | 26.93 | 19.3% |
| DiT4SR w/   UZ-ST | 23.17 | 0.767 | 0.215 | 0.159 | 20.58 | 23.7% |
| Ours w/o UZ-ST | 22.96 | 0.782 | 0.341 | 0.253 | 33.78 | 40.0% |
| Ours w/   UZST | 25.48 | 0.830 | 0.196 | 0.156 | 20.01 | 43.0% |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Methods | PSNR↑\uparrow | SSIM↑\uparrow | LPIPS↓\downarrow | DISTS↓\downarrow | FID↓\downarrow | OCR-A↑\uparrow |
| TADiSR | 24.68 | 0.795 | 0.362 | 0.227 | 52.13 | 35.5% |
| Null Text | 25.59 | 0.834 | 0.188 | 0.151 | 28.93 | 40.4% |
| Random Text | 25.60 | 0.833 | 0.188 | 0.150 | 28.92 | 40.3% |
| Predicted Text (Ours) | 25.63 | 0.834 | 0.185 | 0.150 | 28.82 | 44.6% |

Effectiveness of the training set.
[Tab. 4](#S5.T4 "In 5.3 Ablation Study ‣ 5 Experiment ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") reports consistent OCR-A improvements across different architectures, including the UNet-based OSEDiff and the DiT-based DiT4SR.
This demonstrates that even models without explicit mechanisms for text structure modeling can still learn the mapping from low- to high-resolution text using our dataset, further validating its effectiveness.
Due to their lack of a dedicated mechanism for text structure modeling, they cannot outperform our methods.

OCR Influence.
To investigate how OCR prediction affects the accuracy of our framework, we set the predicted text by OCR in stage 1 as null text or random text and test them on the 35mm subset of UZ-ST.
As shown in [Tab. 5](#S5.T5 "In 5.3 Ablation Study ‣ 5 Experiment ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), even without the OCR model’s predicted text, our method attains a strong OCR-A score of 40.4%, outperforming TAiDSR.
This demonstrates that our model in stage 1 benefits from the inherent text structure in the LR input to restore text structure and is not overly dependent on the OCR model.

Effectiveness of the TiGeSR component.
We set stage 2 as the fixed baseline for image restoration and validate the effectiveness of our framework through 4 ablated variants:

Empty Mask Guidance.
As shown in [Tab. 4](#S5.T4 "In 5.3 Ablation Study ‣ 5 Experiment ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), empty masks provide zero structure guidance, and the model can only rely on the LR for text restoration. Therefore, the OCR-A drops from 67.3% to 59.5%.

Standard Font Guidance.
As shown in the second column of [Fig. 5](#S5.F5 "In 5.2.1 Quantitative Results ‣ 5.2 Comparison Results ‣ 5 Experiment ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), the standard font, while structurally correct, provides weak guidance due to style and position mismatches.
As a result, the restored text exhibits poor accuracy compared to TiGeSR, with the OCR-A dropping from 67.1% to 55.3%, as shown in [Tab. 6](#S5.T6 "In 5.3 Ablation Study ‣ 5 Experiment ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance").

SAM-TS Extraction [[19](#bib.bib19), [49](#bib.bib49)].
While this improves visual quality by better aligning output masks with the LR image, SAM-TS can only extract distorted structures and can’t recover degraded text ([Fig. 5](#S5.F5 "In 5.2.1 Quantitative Results ‣ 5.2 Comparison Results ‣ 5 Experiment ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), third column), leading to suboptimal performance compared with TiGeSR, with OCR-A dropping from 0.671 to 0.579.

LDM Guidance.
This variant uses a latent diffusion model conditioned on LR to restore text structure, achieving better accuracy by reconstructing or compensating for lost text.
However, without separate learning from synthetic and real-world data, it struggles with high-quality text structures in real-world scenarios.
As shown in [Fig. 5](#S5.F5 "In 5.2.1 Quantitative Results ‣ 5.2 Comparison Results ‣ 5 Experiment ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), fourth column, the masks remain noisy under real-world degradations, leading to lower accuracy than TiGeSR, with OCR-A dropping from 67.1% to 60.1% as reported in [Tab. 6](#S5.T6 "In 5.3 Ablation Study ‣ 5 Experiment ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance").

Our method uses RGB output to jointly learn from real-world degradations and accurate synthetic masks, yielding high-quality masks and achieving the highest accuracy.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Text Mask Settings | PSNR↑\uparrow | SSIM↑\uparrow | LPIPS↓\downarrow | DISTS↓\downarrow | FID↓\downarrow | OCR-A↑\uparrow |
| Empty Mask | 23.33 | 0.792 | 0.225 | 0.172 | 42.93 | 59.5% |
| Std Font Guidance | 23.31 | 0.786 | 0.249 | 0.164 | 41.83 | 55.3% |
| SAM-TS Extraction | 23.91 | 0.835 | 0.212 | 0.147 | 41.22 | 57.9% |
| LDM Guidance | 22.42 | 0.798 | 0.222 | 0.147 | 43.08 | 60.1% |
| TiGeSR (Ours) | 24.12 | 0.839 | 0.164 | 0.125 | 38.72 | 67.3% |

## B-e8989777aaf08d

https://arxiv.org/html/2510.21590#chars-37735-38685

## 6 Conclusion

In this paper, we delve into the extensively researched problem of scene text super-resolution.
To address this challenge, we propose a novel approach, TiGeSR, that decouples glyph structure restoration from image enhancement.
For the restoration of text structure, we propose the text restoration pipeline, which enables a 2-phase training strategy to fully take advantage of both synthetic and real-world data.
For the image enhancement, we propose the image enhancement pipeline, which effectively utilizes the glyph structure to restore both text fidelity
and image details coherently in full-image super-resolution.
In terms of training data and benchmark, we present the UltraZoom-ST, the first real-world scene text dataset with a maximum zooming of ×14.29\times 14.29,
offering more challenging scenarios for the field.
Extensive experiments on Real-CE and UZ-ST demonstrate the superiority of TiGeSR over existing methods.

## B-eab9c0871e8820

https://arxiv.org/html/2510.21590#chars-0-209

##### Report GitHub Issue

Content selection saved. Describe the issue below:

![](/static/base/1.0.1/images/icons/smileybones-small.svg)
![arXiv logo](/static/base/1.0.1/images/arxiv-logo-primary-light.svg)

## B-f1e35de8dd6221

https://arxiv.org/html/2510.21590#chars-27823-27851

### 5.2 Comparison Results

## B-f36b0e5edc96d2

https://arxiv.org/html/2510.21590#chars-53148-54579

## 14 Additional results

We provide detailed quantitative results of UZ-ST in [Tab. 11](#Sx1.T11 "In Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance").
Additional qualitative results are provided in [Fig. 7](#S15.F7 "In 15 Efficiency Analysis ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") and [Fig. 8](#S15.F8 "In 15 Efficiency Analysis ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance").
[Fig. 9](#S15.F9 "In 15 Efficiency Analysis ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") also shows the ability of our method in handling other languages like Japanese and Korean.

We also conduct additional ablation experiment on how the randomness of OCR output affect our method.
As shown in [Tab. 10](#Sx1.T10 "In Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance"), the text accuracy gains as the randomness of the OCR output declines.
However, even under complete random OCR prediction, our method still manage to outperform TADiSR thanks to the LR condition still guiding the stage 1 to generate text structures.
This proves that the reliance of our method on the OCR model is limited.

## B-f78c0a500ab2b1

https://arxiv.org/html/2510.21590#chars-12007-16754

### 3.2 Text Restoration stage

![Refer to caption](2510.21590v3/datapipeV7.png)

Text Restoration Pipeline.
Existing methods like Hi-SAM [[49](#bib.bib49)] work well on clean high-resolution text but fail on the incomplete, distorted text in low-resolution images.
To address this, we propose a region-level text restoration pipeline shown in [Fig. 2](#S2.F2 "In 2 Related Works ‣ Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance") built on [[35](#bib.bib35)] to recover glyph structures xm∈ℝH×W×Cx\_{m}\in\mathbb{R}^{H\times W\times C}.
An OCR detector first localizes text regions {xL0,…,xLN−1}\{x^{0}\_{L},...,x^{N-1}\_{L}\} and extracts their contents {y0,…,yN−1}\{y^{0},...,y^{N-1}\} as semantic conditions.
Each region x~L\tilde{x}\_{L} is encoded by VAE [[21](#bib.bib21)] into z~L∈ℝh×w×c\tilde{z}\_{L}\in\mathbb{R}^{h\times w\times c}, concatenated with noise zT∈ℝh×w×2​cz\_{T}\in\mathbb{R}^{h\times w\times 2c}, and iteratively denoised by a UNet ϵθ\epsilon\_{\theta} into two branches: zt−1R​G​B∈ℝh×w×cz^{RGB}\_{t-1}\in\mathbb{R}^{h\times w\times c} for appearance and zt−1m∈ℝh×w×cz^{m}\_{t-1}\in\mathbb{R}^{h\times w\times c} for structure, which are merged as zt−1z\_{t-1}.
The text content yy is embedded into ct​ec\_{te} and fused into ztz\_{t} via cross-attention to guide structure recovery. After TT denoising steps, the mask branch output z0mz^{m}\_{0} is decoded into x~m\tilde{x}\_{m}, and all restored regions are assembled into the final text mask x^m\hat{x}\_{m}.
Focusing on real text reconstruction enables the model to capture glyph structures without non-text interference and reduces sensitivity to text saliency.

Training Strategy. The scarcity of real-world segmentation masks for degraded text forces reliance on synthetic data, yet its artificial degradation limits generalization.
Annotating real degraded samples, however, is labor-intensive and costly.
To marry synthetic precision with real-world degradation, we propose a two-phase training strategy.
In Phase 1, both synthetic and real data are included in training.
This allows the model to generate text masks from the LR image and capture real-world degradation patterns.
However, noisy masks in real data degrade mask quality.
To address this, we freeze the RGB out block and the mask out block and train the UNet with only synthetic data to refine the quality of output text masks in Phase 2.
The training objective is described as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=λt​d​ℒt​d+λS​e​g​ℒS​e​g,\mathcal{L}=\lambda\_{td}\mathcal{L}\_{td}+\lambda\_{Seg}\mathcal{L}\_{Seg}, |  | (1) |

where ℒt​d\mathcal{L}\_{td}, ℒS​e​g\mathcal{L}\_{Seg}, λt​d\lambda\_{td}, and λS​e​g\lambda\_{Seg} denote the text-control diffusion loss, segmentation-oriented loss, and their corresponding hyperparameters. The text-control diffusion loss is formulated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒϵ=𝔼z0,z~L,ct​e,t,ϵ∼𝒩⁡(0,1)​[‖ϵ−ϵθ​(zt,z~L,ct​e,t)‖22].\mathcal{L}\_{\epsilon}=\mathbb{E}\_{\textbf{{z}}\_{0},\tilde{\textbf{{z}}}\_{L},\textbf{{c}}\_{te},\textbf{{t}},\epsilon\sim\mathcal{N}(0,1)}\left[\|\epsilon-\epsilon\_{\theta}(\textbf{{z}}\_{t},\tilde{\textbf{{z}}}\_{L},\textbf{{c}}\_{te},\textbf{{t}})\|\_{2}^{2}\right]. |  | (2) |

To improve the quality of the text mask, we propose a segmentation-oriented loss. Let εt\mathcal{\varepsilon}\_{t} denote the noise predicted by the denoiser network ϵθ\epsilon\_{\theta}.
Following  [[18](#bib.bib18)], z0mz^{m}\_{0} can be estimated by combining the time step tt with the noisy latent image ztmz^{m}\_{t}.
This estimate is subsequently passed through the VAE decoder to obtain an approximate reconstruction of the original input text mask, denoted as x0′mx^{\prime m}\_{0}.
In this way, text mask generation can be supervised at the pixel level.
We combine Mean Squared Error (MSE), Focal, and Dice Losses, commonly used in segmentation tasks [[49](#bib.bib49)], to compare x0′mx^{\prime m}\_{0} with the original image x0mx^{m}\_{0}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒS​e​g=‖x0′m−x0m‖22+λF​o​c​a​l​FocalLoss​(x0′m,x0m)\displaystyle\mathcal{L}\_{Seg}=\|x^{\prime m}\_{0}-x^{m}\_{0}\|^{2}\_{2}+\lambda\_{Focal}\text{FocalLoss}(x^{\prime m}\_{0},x^{m}\_{0}) |  | (3) |
|  | +λD​i​c​e​DiceLoss​(x0′m,x0m),\displaystyle+\lambda\_{Dice}\text{DiceLoss}(x^{\prime m}\_{0},x^{m}\_{0}), |  |

where λF​o​c​a​l\lambda\_{Focal} and λD​i​c​e\lambda\_{Dice} are their respective balancing coefficients.
This combination forms a novel text-first paradigm that equips the model with both structural accuracy and real-world generalization, laying the foundation for the subsequent full-image super-resolution stage.

## B-fb672ca5ff5013

https://arxiv.org/html/2510.21590#chars-47848-48049

## 9 LLM Acknowledgments

We thank ChatGPT (GPT-5) and DeepSeek for the help in refining the language and improving clarity.
All wording and factual content were reviewed and approved by the authors.

## B-ocr-271ae0778aedbd

B PDF page 7

(a) Visual comparison on Real-CE. Our decoupling strategy yields superior performance on small text.

![img-2.jpeg](img-2.jpeg)

(b) Visual comparison on UZ-ST, showing robustness to severe degradation with 2-phase training.

![img-3.jpeg](img-3.jpeg)

Figure 4. Qualitative Evaluation on Real-CE and UZ-ST.

### 5.3. Ablation Study

Effectiveness of the training set. Tab. 4 reports consistent OCR-A improvements across different architectures, including the UNet-based OSEDiff and the DiT-based DiT4SR. This demonstrates that even models without explicit mechanisms for text structure modeling can still learn the mapping from low- to high-resolution text using our dataset, further validating its effectiveness. Due to their lack of a dedicated mechanism for text structure modeling, they

cannot outperform our methods.

OCR Influence. To investigate how OCR prediction affects the accuracy of our framework, we set the predicted text by OCR in stage 1 as null text or random text and test them on the 35mm subset of UZ-ST. As shown in Tab. 5, even without the OCR model's predicted text, our method attains a strong OCR-A score of 40.4%, outperforming TAIiDSR. This demonstrates that our model in stage 1 benefits from the inherent text structure in the LR input to restore text structure and is not overly dependent on the OCR model.

## B-ocr-3b9570c4b0e6ab

B PDF page 15

Table 11. Evaluation Results on Both Image Quality and Text Accuracy on UltraZoom-ST.

[tbl-3.html](tbl-3.html)

[OCR table id=tbl-3.html; page=15]
<table><tr><td></td><td>Methods</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>DISTS↓</td><td>FID↓</td><td>PSNR<sub>CT</sub>↑</td><td>SSIM<sub>CT</sub>↑</td><td>LPIPS<sub>CT</sub>↓</td><td>DISTS<sub>CT</sub>↓</td><td>OCR-A↑</td></tr><tr><td rowspan="13">85mm (×2.35)</td><td>Real-ESRGAN</td><td>25.84</td><td>0.854</td><td>0.139</td><td>0.130</td><td>28.25</td><td>23.59</td><td>0.843</td><td>0.170</td><td>0.168</td><td>60.8%</td></tr><tr><td>HAT</td><td>27.33</td><td>0.873</td><td>0.128</td><td>0.133</td><td>27.21</td><td>24.76</td><td>0.870</td><td>0.139</td><td>0.146</td><td>62.0%</td></tr><tr><td>MACRONet</td><td>22.90</td><td>0.804</td><td>0.234</td><td>0.173</td><td>40.19</td><td>17.92</td><td>0.693</td><td>0.515</td><td>0.360</td><td>54.2%</td></tr><tr><td>SeeSR</td><td>25.02</td><td>0.826</td><td>0.167</td><td>0.159</td><td>32.31</td><td>21.62</td><td>0.796</td><td>0.245</td><td>0.207</td><td>28.2%</td></tr><tr><td>SupIR</td><td>25.58</td><td>0.823</td><td>0.202</td><td>0.160</td><td>29.33</td><td>21.91</td><td>0.808</td><td>0.239</td><td>0.214</td><td>33.3%</td></tr><tr><td>DiffTSR</td><td>23.48</td><td>0.805</td><td>0.230</td><td>0.157</td><td>35.77</td><td>17.92</td><td>0.688</td><td>0.392</td><td>0.285</td><td>48.2%</td></tr><tr><td>DiffBIR</td><td>25.25</td><td>0.793</td><td>0.175</td><td>0.152</td><td>24.57</td><td>22.26</td><td>0.803</td><td>0.218</td><td>0.190</td><td>36.8%</td></tr><tr><td>OSEDiff</td><td>26.38</td><td>0.852</td><td>0.153</td><td>0.137</td><td>23.92</td><td>22.84</td><td>0.833</td><td>0.200</td><td>0.204</td><td>41.0%</td></tr><tr><td>DreamClear</td><td>25.31</td><td>0.811</td><td>0.169</td><td>0.151</td><td>24.19</td><td>21.44</td><td>0.790</td><td>0.253</td><td>0.221</td><td>26.8%</td></tr><tr><td>TSD-SR</td><td>23.99</td><td>0.800</td><td>0.161</td><td>0.165</td><td>30.40</td><td>20.62</td><td>0.786</td><td>0.232</td><td>0.218</td><td>37.8%</td></tr><tr><td>DiT4SR</td><td>24.71</td><td>0.810</td><td>0.173</td><td>0.143</td><td>29.15</td><td>21.25</td><td>0.800</td><td>0.221</td><td>0.193</td><td>48.2%</td></tr><tr><td>TADiSR</td><td>26.31</td><td>0.858</td><td>0.177</td><td>0.149</td><td>30.47</td><td>23.55</td><td>0.856</td><td>0.175</td><td>0.178</td><td>55.7%</td></tr><tr><td>Ours</td><td>27.00</td><td>0.871</td><td>0.123</td><td>0.120</td><td>22.34</td><td>24.31</td><td>0.860</td><td>0.135</td><td>0.142</td><td>63.2%</td></tr><tr><td rowspan="13">35mm (×5.71)</td><td>Real-ESRGAN</td><td>23.70</td><td>0.785</td><td>0.218</td><td>0.184</td><td>42.62</td><td>20.86</td><td>0.782</td><td>0.272</td><td>0.235</td><td>34.1%</td></tr><tr><td>HAT</td><td>25.05</td><td>0.819</td><td>0.207</td><td>0.182</td><td>41.32</td><td>21.98</td><td>0.816</td><td>0.250</td><td>0.241</td><td>34.6%</td></tr><tr><td>MACRONet</td><td>22.28</td><td>0.774</td><td>0.284</td><td>0.199</td><td>49.14</td><td>17.43</td><td>0.694</td><td>0.523</td><td>0.361</td><td>31.5%</td></tr><tr><td>SeeSR</td><td>23.76</td><td>0.795</td><td>0.198</td><td>0.175</td><td>37.92</td><td>20.55</td><td>0.778</td><td>0.271</td><td>0.222</td><td>25.2%</td></tr><tr><td>SupIR</td><td>23.49</td><td>0.746</td><td>0.302</td><td>0.204</td><td>41.80</td><td>20.00</td><td>0.757</td><td>0.335</td><td>0.282</td><td>24.0%</td></tr><tr><td>DiffTSR</td><td>22.57</td><td>0.773</td><td>0.281</td><td>0.184</td><td>45.78</td><td>16.99</td><td>0.671</td><td>0.443</td><td>0.312</td><td>31.2%</td></tr><tr><td>DiffBIR</td><td>23.76</td><td>0.731</td><td>0.245</td><td>0.196</td><td>35.99</td><td>20.82</td><td>0.770</td><td>0.275</td><td>0.234</td><td>28.6%</td></tr><tr><td>OSEDiff</td><td>25.35</td><td>0.827</td><td>0.192</td><td>0.166</td><td>29.06</td><td>21.62</td><td>0.809</td><td>0.263</td><td>0.263</td><td>29.9%</td></tr><tr><td>DreamClear</td><td>24.20</td><td>0.778</td><td>0.209</td><td>0.177</td><td>32.08</td><td>20.66</td><td>0.779</td><td>0.283</td><td>0.251</td><td>23.9%</td></tr><tr><td>TSD-SR</td><td>22.93</td><td>0.757</td><td>0.200</td><td>0.199</td><td>37.61</td><td>19.64</td><td>0.760</td><td>0.282</td><td>0.246</td><td>27.3%</td></tr><tr><td>DiT4SR</td><td>23.45</td><td>0.774</td><td>0.204</td><td>0.158</td><td>31.73</td><td>20.12</td><td>0.779</td><td>0.250</td><td>0.208</td><td>26.5%</td></tr><tr><td>TADiSR</td><td>24.68</td><td>0.795</td><td>0.362</td><td>0.227</td><td>52.13</td><td>21.57</td><td>0.798</td><td>0.366</td><td>0.347</td><td>35.5%</td></tr><tr><td>Ours</td><td>25.63</td><td>0.834</td><td>0.185</td><td>0.150</td><td>28.82</td><td>22.14</td><td>0.823</td><td>0.204</td><td>0.194</td><td>44.6%</td></tr><tr><td rowspan="13">14mm (×14.29)</td><td>Real-ESRGAN</td><td>22.09</td><td>0.718</td><td>0.423</td><td>0.284</td><td>89.22</td><td>18.87</td><td>0.721</td><td>0.503</td><td>0.427</td><td>11.5%</td></tr><tr><td>HAT</td><td>22.66</td><td>0.738</td><td>0.451</td><td>0.299</td><td>89.58</td><td>19.27</td><td>0.738</td><td>0.533</td><td>0.484</td><td>12.2%</td></tr><tr><td>MACRONet</td><td>21.00</td><td>0.716</td><td>0.422</td><td>0.254</td><td>79.67</td><td>17.01</td><td>0.680</td><td>0.553</td><td>0.382</td><td>10.1%</td></tr><tr><td>SeeSR</td><td>21.79</td><td>0.731</td><td>0.310</td><td>0.228</td><td>64.31</td><td>18.87</td><td>0.717</td><td>0.396</td><td>0.308</td><td>13.2%</td></tr><tr><td>SupIR</td><td>21.38</td><td>0.681</td><td>0.447</td><td>0.268</td><td>70.09</td><td>17.99</td><td>0.690</td><td>0.487</td><td>0.383</td><td>11.0%</td></tr><tr><td>DiffTSR</td><td>20.88</td><td>0.713</td><td>0.412</td><td>0.233</td><td>74.07</td><td>15.87</td><td>0.630</td><td>0.538</td><td>0.348</td><td>12.0%</td></tr><tr><td>DiffBIR</td><td>21.61</td><td>0.630</td><td>0.392</td><td>0.255</td><td>69.64</td><td>18.61</td><td>0.685</td><td>0.438</td><td>0.328</td><td>11.3%</td></tr><tr><td>OSEDiff</td><td>23.11</td><td>0.768</td><td>0.274</td><td>0.214</td><td>49.76</td><td>19.44</td><td>0.740</td><td>0.385</td><td>0.334</td><td>12.7%</td></tr><tr><td>DreamClear</td><td>22.45</td><td>0.719</td><td>0.364</td><td>0.260</td><td>62.95</td><td>19.14</td><td>0.725</td><td>0.440</td><td>0.377</td><td>11.7%</td></tr><tr><td>TSD-SR</td><td>21.14</td><td>0.705</td><td>0.273</td><td>0.225</td><td>57.07</td><td>17.67</td><td>0.686</td><td>0.393</td><td>0.293</td><td>11.9%</td></tr><tr><td>DiT4SR</td><td>20.88</td><td>0.707</td><td>0.282</td><td>0.181</td><td>47.45</td><td>17.36</td><td>0.687</td><td>0.367</td><td>0.253</td><td>11.7%</td></tr><tr><td>TADiSR</td><td>22.43</td><td>0.721</td><td>0.555</td><td>0.320</td><td>98.44</td><td>19.20</td><td>0.730</td><td>0.585</td><td>0.518</td><td>14.4%</td></tr><tr><td>Ours</td><td>23.41</td><td>0.774</td><td>0.301</td><td>0.209</td><td>54.74</td><td>19.73</td><td>0.748</td><td>0.374</td><td>0.322</td><td>16.0%</td></tr><tr><td rowspan="13">Total</td><td>RealEsrGAN</td><td>23.99</td><td>0.790</td><td>0.248</td><td>0.194</td><td>30.60</td><td>21.25</td><td>0.786</td><td>0.302</td><td>0.266</td><td>37.1%</td></tr><tr><td>HAT</td><td>25.17</td><td>0.815</td><td>0.249</td><td>0.198</td><td>30.12</td><td>22.18</td><td>0.813</td><td>0.291</td><td>0.276</td><td>37.9%</td></tr><tr><td>MARCONet</td><td>22.13</td><td>0.768</td><td>0.306</td><td>0.205</td><td>34.28</td><td>17.48</td><td>0.690</td><td>0.529</td><td>0.366</td><td>33.4%</td></tr><tr><td>SeeSR</td><td>23.64</td><td>0.788</td><td>0.219</td><td>0.184</td><td>26.73</td><td>20.45</td><td>0.767</td><td>0.297</td><td>0.241</td><td>22.8%</td></tr><tr><td>SupIR</td><td>23.62</td><td>0.754</td><td>0.308</td><td>0.207</td><td>27.91</td><td>20.10</td><td>0.756</td><td>0.344</td><td>0.287</td><td>23.6%</td></tr><tr><td>DiffTSR</td><td>22.41</td><td>0.767</td><td>0.300</td><td>0.189</td><td>31.25</td><td>17.00</td><td>0.665</td><td>0.452</td><td>0.313</td><td>31.7%</td></tr><tr><td>DiffBIR</td><td>23.67</td><td>0.724</td><td>0.262</td><td>0.197</td><td>23.10</td><td>20.70</td><td>0.757</td><td>0.302</td><td>0.245</td><td>26.6%</td></tr><tr><td>OSEDiff</td><td>25.07</td><td>0.819</td><td>0.201</td><td>0.169</td><td>20.53</td><td>21.43</td><td>0.798</td><td>0.276</td><td>0.263</td><td>28.9%</td></tr><tr><td>DreamClear</td><td>24.10</td><td>0.773</td><td>0.238</td><td>0.191</td><td>21.75</td><td>20.50</td><td>0.768</td><td>0.317</td><td>0.276</td><td>21.4%</td></tr><tr><td>TSD-SR</td><td>22.79</td><td>0.757</td><td>0.207</td><td>0.194</td><td>24.08</td><td>19.42</td><td>0.748</td><td>0.296</td><td>0.249</td><td>26.6%</td></tr><tr><td>DiT4SR</td><td>23.16</td><td>0.767</td><td>0.215</td><td>0.159</td><td>20.58</td><td>19.73</td><td>0.760</td><td>0.273</td><td>0.216</td><td>23.7%</td></tr><tr><td>TADiSR</td><td>24.61</td><td>0.796</td><td>0.203</td><td>0.160</td><td>36.61</td><td>21.59</td><td>0.799</td><td>0.360</td><td>0.336</td><td>36.6%</td></tr><tr><td>Ours</td><td>25.48</td><td>0.830</td><td>0.196</td><td>0.156</td><td>20.01</td><td>22.22</td><td>0.814</td><td>0.228</td><td>0.212</td><td>43.0%</td></tr></table>

## B-ocr-5fe967d02f4fdf

B PDF page 4

![img-1.jpeg](img-1.jpeg)

Figure 3. Overview of UZ-ST (UltraZoom-Scene Text). (a) Real-CE LRs show only mild degradation (red box), while UZ-ST LRs exhibit stronger degradation (red box), enabling a more comprehensive evaluation. (b) Coarse-to-fine alignment: images are sorted by focal length, each warped to the next higher-focal neighbor using an estimated homography matrix, then refined to the \(200\mathrm{mm}\) GT.

as \( z_{t-1} \). The text content \( y \) is embedded into \( c_{te} \) and fused into \( z_t \) via cross-attention to guide structure recovery. After \( T \) denoising steps, the mask branch output \( z_0^m \) is decoded into \( \hat{x}_m \), and all restored regions are assembled into the final text mask \( \hat{x}_m \). Focusing on real text reconstruction enables the model to capture glyph structures without non-text interference and reduces sensitivity to text saliency.

Training Strategy. The scarcity of real-world segmentation masks for degraded text forces reliance on synthetic data, yet its artificial degradation limits generalization. Annotating real degraded samples, however, is labor-intensive and costly. To marry synthetic precision with real-world degradation, we propose a two-phase training strategy. In Phase 1, both synthetic and real data are included in training. This allows the model to generate text masks from the LR image and capture real-world degradation patterns. However, noisy masks in real data degrade mask quality. To address this, we freeze the RGB out block and the mask out block and train the UNet with only synthetic data to refine the quality of output text masks in Phase 2. The training objective is described as follows:

\[
\mathcal {L} = \lambda_ {t d} \mathcal {L} _ {t d} + \lambda_ {S e g} \mathcal {L} _ {S e g}, \tag {1}
\]

where  \( L_{td} \) ,  \( L_{Seg} \) ,  \( \lambda_{td} \) , and  \( \lambda_{Seg} \)  denote the text-control diffusion loss, segmentation-oriented loss, and their corresponding hyperparameters. The text-control diffusion loss is formulated as follows:

\[
\mathcal {L} _ {\epsilon} = \mathbb {E} _ {\boldsymbol {z} _ {0}, \hat {\boldsymbol {z}} _ {L}, \boldsymbol {c} _ {t e}, t, \epsilon \sim \mathcal {N} (0, 1)} \left[ \| \epsilon - \epsilon_ {\theta} (\boldsymbol {z} _ {t}, \hat {\boldsymbol {z}} _ {L}, \boldsymbol {c} _ {t e}, t) \| _ {2} ^ {2} \right]. \tag {2}
\]

To improve the quality of the text mask, we propose a segmentation-oriented loss. Let \(\varepsilon_{t}\) denote the noise predicted by the denoiser network \(\epsilon_{\theta}\). Following [18], \(z_0^m\)

can be estimated by combining the time step \( t \) with the noisy latent image \( z_{t}^{m} \). This estimate is subsequently passed through the VAE decoder to obtain an approximate reconstruction of the original input text mask, denoted as \( x_0^{\prime m} \). In this way, text mask generation can be supervised at the pixel level. We combine Mean Squared Error (MSE), Focal, and Dice Losses, commonly used in segmentation tasks [49], to compare \( x_0^{\prime m} \) with the original image \( x_0^m \):

\[
\begin{array}{l} \mathcal {L} _ {\text {Seg}} = \left\| x _ {0} ^ {\prime m} - x _ {0} ^ {m} \right\| _ {2} ^ {2} + \lambda_ {\text {Focal}} \text {FocalLoss} \left(x _ {0} ^ {\prime m}, x _ {0} ^ {m}\right) \tag {3} \\ + \lambda_ {D i c e} \text { DiceLoss } (x _ {0} ^ {\prime m}, x _ {0} ^ {m}), \\ \end{array}
\]

where  \( \lambda_{Focal} \)  and  \( \lambda_{Dice} \)  are their respective balancing coefficients. This combination forms a novel text-first paradigm that equips the model with both structural accuracy and real-world generalization, laying the foundation for the subsequent full-image super-resolution stage.

### 3.3. Image Enhancement stage

Image Enhancement pipeline. To effectively take advantage of the generated glyph structure  \( \hat{x}_{m} \)  and enhance the quality of LR  \( x_{L} \) , we adopt a ControlNet [56] network  \( \epsilon_{\phi} \) . As illustrated in Fig. 2, after getting their latent representation  \( \hat{z}_{m} \)  and  \( z_{L} \) , we use the network to denoise the  \( z_{L} \)  only at the specific timestep t, using the null-text embedding  \( c_{Null} \) . The output super-resolved latent representation  \( \hat{z}_{H} \)  will be denoted as:

\[
\hat {z} _ {H} = z _ {L} - \sigma_ {t} \epsilon_ {\phi} (z _ {L}, \hat {z} _ {m}, t, c _ {N u l l}), \tag {4}
\]

where  \( \sigma_{t} \)  is a scalar determined by the predefined diffusion time step. With the text restoration stage, this image enhancement pipeline forms a progressive ‘text-first, image

## B-ocr-675a47be4c8378

B PDF page 17

![img-16.jpeg](img-16.jpeg)

Figure 8. Additional qualitative results of TiGeSR.

## B-ocr-71d67150e1ef7b

B PDF page 14

Table 9. Efficiency analysis.

[tbl-1.html](tbl-1.html)

Table 10. Ablation on the effect of stochastic OCR outputs on the performance of our method. The performance gains as the randomness of the OCR output drops. Even under \(100\%\) random OCR output, our method still outperforms TADiSR, proving low reliance on OCR.

[tbl-2.html](tbl-2.html)

RealSR

![img-4.jpeg](img-4.jpeg)

SIFT alignment (Single time)

![img-5.jpeg](img-5.jpeg)

Ours

![img-6.jpeg](img-6.jpeg)

GT

![img-7.jpeg](img-7.jpeg)

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

![img-12.jpeg](img-12.jpeg)

![img-13.jpeg](img-13.jpeg)

![img-14.jpeg](img-14.jpeg)

![img-15.jpeg](img-15.jpeg)

Figure 6. Alignment method comparison.

[OCR table id=tbl-1.html; page=14]
<table><tr><td>Methods</td><td>Flops (GFLOPs)</td><td>Speed (ms)</td><td>OCR-A</td></tr><tr><td>HAT</td><td>6670.32</td><td>1086.68</td><td>37.9%</td></tr><tr><td>DiffTSR</td><td>58502.14</td><td>8610.59</td><td>31.7%</td></tr><tr><td>DiT4SR w/o llava</td><td>160787.14</td><td>17385.14</td><td>23.7%</td></tr><tr><td>DreamClear w/o llava</td><td>412843.67</td><td>83193.81</td><td>21.4%</td></tr><tr><td>TADiSR</td><td>4497.96</td><td>342.32</td><td>36.6%</td></tr><tr><td>TiGeSR (ours) Stage 1</td><td>6215.85</td><td>663.5</td><td rowspan="2">43.0%</td></tr><tr><td>TiGeSR (ours) Stage 2</td><td>3734.01</td><td>360.06</td></tr></table>

[OCR table id=tbl-2.html; page=14]
<table><tr><td>Methods</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>DISTS↓</td><td>FID↓</td><td>OCR-A↑</td></tr><tr><td>TADiSR</td><td>24.68</td><td>0.795</td><td>0.362</td><td>0.227</td><td>52.13</td><td>35.5%</td></tr><tr><td colspan="7">TiGeSR (Ours) performance under different randomness of OCR output.</td></tr><tr><td>100% Random Text</td><td>25.60</td><td>0.833</td><td>0.188</td><td>0.150</td><td>28.92</td><td>40.3%</td></tr><tr><td>50% Random Text</td><td>25.60</td><td>0.833</td><td>0.189</td><td>0.151</td><td>28.92</td><td>40.6%</td></tr><tr><td>20% Random Text</td><td>25.63</td><td>0.834</td><td>0.185</td><td>0.150</td><td>29.3</td><td>43.7%</td></tr><tr><td>0% Random Text (Ours)</td><td>25.63</td><td>0.834</td><td>0.185</td><td>0.150</td><td>28.82</td><td>44.6%</td></tr></table>

## B-ocr-7a9d40e19fd320

B PDF page 1

arXiv:2510.21590v3 [cs.CV] 3 Aug 2026

# Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance

Minxing Luo \( ^{1,2,*} \) , Linlong Fan \( ^{2,*} \) , Qiushi Wang \( ^{2,3} \) , Ge Wu \( ^{1} \) , Yiyan Luo \( ^{2} \) , Yuhang Yu \( ^{2} \) , Jinwei Chen \( ^{2} \) , Yaxing Wang \( ^{1,4} \) , Qingnan Fan \( ^{2,\dagger} \) , Jian Yang \( ^{1,5,\dagger} \)

\( ^{1} \) PCA Lab, VCIP, College of Computer Science, Nankai University  \( ^{2} \) vivo BlueImage Lab, vivo Mobile Communication Co., Ltd.  \( ^{3} \) SDS, CUHK, Shenzhen  \( ^{4} \) NKIARI, Shenzhen Futian  \( ^{5} \) PCA Lab, School of Intelligence Science and Technology, Nanjing University

(a) Real World Samples

![img-0.jpeg](img-0.jpeg)

Figure 1. We present TiGeSR (Text–Image Guided Super-Resolution), a novel framework for scene text super-resolution. Its ‘text-first, image-later’ paradigm ensures accurate glyph restoration and consistently high overall image fidelity and visual quality.

## Abstract

Current image super-resolution methods show strong performance on natural images but distort text, creating a fundamental trade-off between image quality and textual readability. To address this, we introduce TiGeSR (Text–Image Guided Super-Resolution), a two-stage framework that breaks this trade-off through a “text-first, image-later” paradigm. TiGeSR explicitly decouples glyph restoration from image enhancement: it first reconstructs precise text structures and uses them to guide full-image super-resolution. This ensures high fidelity and readability. For comprehensive training and evaluation, we present the UZ-ST (UltraZoom-Scene Text) dataset, the first Chinese scene text dataset with highest zoom of ×14.29. Extensive experiments show TiGeSR achieves state-of-the-art

performance, enhancing readability and image quality.

## 1. Introduction

Scene Text Image Super-Resolution is a critical problem in computer vision for its vital role in downstream applications  \( [8, 20, 24, 37] \) . It seeks to restore a high-quality super-resolution (SR) image from a degraded low-resolution (LR) input while preserving the text meaning. Unlike general image super-resolution for natural scenes, where plausible texture synthesis or detail hallucination is acceptable and does not alter the semantic meaning of the image, visual texts exhibit extremely low tolerance to structural errors. This is especially evident in Chinese, where a minor stroke distortion or omission may entirely alter the meaning  \( [25, 52] \) .

In recent years, with the rapid development of generative models such as diffusion  \( [3, 9, 18, 33, 35, 36, 59] \) , image super-resolution has increasingly relied on their strong generative priors to recover missing details from low-resolution

## B-ocr-859355e3c3f54e

B PDF page 9

## Acknowledgement

This work was supported by the NSFC under Grant Nos. 62361166670, U24A20330, Shenzhen Science and Technology Program (JCYJ20240813114237048), "Science and Technology Yongjiang 2035" key technology breakthrough plan project (2024Z120), Chinese government-guided local science and technology development fund projects (scientific and technological achievement transfer and transformation projects) (254Z0102G).

## References

[1] Yuang Ai, Xiaoqiang Zhou, Huaibo Huang, Xiaotian Han, Zhengyu Chen, Quanzeng You, and Hongxia Yang. Dream-clear: High-capacity real-world image restoration with privacy-safe dataset curation. Advances in Neural Information Processing Systems, 37:55443–55469, 2024. 3, 6

[2] Jianrui Cai, Hui Zeng, Hongwei Yong, Zisheng Cao, and Lei Zhang. Toward real-world single image super-resolution: A new benchmark and a new model. In Proceedings of the IEEE/CVF international conference on computer vision, pages 3086–3095, 2019. 5, 2

[3] Huiwen Chang, Han Zhang, Jarred Barber, Aaron Maschinot, José Lezama, Lu Jiang, Ming-Hsuan Yang, Kevin Patrick Murphy, William T. Freeman, Michael Rubinstein, Yuanzhen Li, and Dilip Krishnan. Muse: Text-to-image generation via masked generative transformers. In International Conference on Machine Learning, ICML 2023, 23-29 July 2023, Honolulu, Hawaii, USA, pages 4055–4075. PMLR, 2023. 1

[4] Jingye Chen, Bin Li, and Xiangyang Xue. Scene text telescope: Text-focused scene image super-resolution. In CVPR, pages 12026–12035, 2021. 3

[5] Xiangyu Chen, Xintao Wang, Jiantao Zhou, Yu Qiao, and Chao Dong. Activating more pixels in image super-resolution transformer. In CVPR, pages 22367-22377, 2023. 5

[6] Kun Cheng, Lei Yu, Zhijun Tu, Xiao He, Liyu Chen, Yong Guo, Mingrui Zhu, Nannan Wang, Xinbo Gao, and Jie Hu. Effective diffusion transformer architecture for image super-resolution. In Proceedings of the AAAI Conference on Artificial Intelligence, pages 2455–2463, 2025. 2

[7] Cheng Cui, Ting Sun, Manhui Lin, Tingquan Gao, Yubo Zhang, Jiaxuan Liu, Xueqing Wang, Zelun Zhang, Changda Zhou, Hongen Liu, Yue Zhang, Wenyu Lv, Kui Huang, Yichao Zhang, Jing Zhang, Jun Zhang, Yi Liu, Dianhai Yu, and Yanjun Ma. Paddleocr 3.0 technical report, 2025. 1

[8] Gayatri Deshmukh, Onkar Susladkar, Dhruv Makwana, Sparsh Mittal, et al. Textual alchemy: Coformer for scene text understanding. In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision, pages 2931–2941, 2024. 1

[9] Prafulla Dhariwal and Alexander Nichol. Diffusion models beat gans on image synthesis. Advances in neural information processing systems, 34:8780–8794, 2021. 1

[10] Keyan Ding, Kede Ma, Shiqi Wang, and Eero P Simoncelli. Image quality assessment: Unifying structure and texture similarity. TPAMI, 44(5):2567–2581, 2020. 5

[11] Chao Dong, Chen Change Loy, Kaiming He, and Xiaoou Tang. Learning a deep convolutional network for image super-resolution. In ECCV, pages 184–199, 2014. 3

[12] Chao Dong, Ximei Zhu, Yubin Deng, Chen Change Loy, and Yu Qiao. Boosting optical character recognition: A super-resolution approach. arXiv preprint, 2015. 3

[13] Linwei Dong, Qingnan Fan, Yihong Guo, Zhonghao Wang, Qi Zhang, Jinwei Chen, Yawei Luo, and Changqing Zou. TSD-SR: one-step diffusion with target score distillation for real-world image super-resolution. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2025, Nashville, TN, USA, June 11-15, 2025, pages 23174–23184. Computer Vision Foundation / IEEE, 2025. 2

[14] Linwei Dong, Qingnan Fan, Yihong Guo, Zhonghao Wang, Qi Zhang, Jinwei Chen, Yawei Luo, and Changqing Zou. Tsd-sr: One-step diffusion with target score distillation for real-world image super-resolution. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 23174–23184, 2025. 2, 6

[15] Zheng-Peng Duan, Jiawei Zhang, Xin Jin, Ziheng Zhang, Zheng Xiong, Dongqing Zou, Jimmy Ren, Chun-Le Guo, and Chongyi Li. Dit4sr: Taming diffusion transformer for real-world image super-resolution. In Proceedings of the IEEE/CVF International Conference on Computer Vision, 2025. 2, 3, 6

[16] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller, Harry Saini, Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, et al. Scaling rectified flow transformers for high-resolution image synthesis. In Forty-first international conference on machine learning, 2024. 5, 1

[17] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. Gans trained by a two time-scale update rule converge to a local nash equilibrium. NeurIPS, 30, 2017. 5

[18] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. Advances in Neural Information Processing Systems, 33:6840–6851, 2020. 1, 4

[19] Qiming Hu, Linlong Fan, Yiyan Luo, Yuhang Yu, Xiaojie Guo, and Qingnan Fan. Text-aware real-world image super-resolution via diffusion model with joint segmentation decoders. arXiv preprint arXiv:2506.04641, 2025. 2, 3, 5, 6, 8, 1

[20] Jihyung Kil, Soravit Changpinyo, Xi Chen, Hexiang Hu, Sebastian Goodman, Wei-Lun Chao, and Radu Soricut. Prestu: Pre-training for scene-text understanding. In Proceedings of the IEEE/CVF international conference on computer vision, pages 15270–15280, 2023. 1

[21] Diederik P Kingma and Max Welling. Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114, 2013. 3

[22] Johannes Künzel, Anna Hilsmann, and Peter Eisert. RIPE: Reinforcement Learning on Unlabeled Image Pairs for Robust Keypoint Extraction. arXiv, 2025. 5

[23] Chenxia Li, Weiwei Liu, Ruoyu Guo, Xiaoting Yin, Kaitao Jiang, Yongkun Du, Yuning Du, Lingfeng Zhu, Baohua Lai,

## B-ocr-8e87dcd10b8aef

B PDF page 5

after' paradigm. Our design injects structure-aware control into the generative process, allowing the network to enhance global image quality while preserving text structures.

Training Strategy. For the quality of image super-resolution, we constrain the reconstruction loss between the predicted high-resolution image  \( \hat{x}_{H} \)  decoded from  \( \hat{z}_{H} \)  by  \( \varepsilon \)  and the ground truth high-resolution image  \( x_{H} \)  using a weighted sum of MSE and LPIPS losses:

\[
\mathcal {L} _ {i m g} = \lambda_ {l 2} \| x _ {H} - \hat {x} _ {H} \| _ {2} ^ {2} + \lambda_ {L P I P S} \mathrm{LPIPS} (x _ {H}, \hat {x} _ {H}), \tag {5}
\]

where \(\lambda_{l2}\) and \(\lambda_{LPIPS}\) are balancing coefficients for different loss terms. To enhance glyph control and emphasize the glyph structure, we extract the text boundaries using Sobel operators [34]. This edge loss is expressed as:

\[
\mathcal {L} _ {\text { edge }} = \left\| \operatorname{Sobel} (x _ {H}) - \operatorname{Sobel} (\hat {x} _ {H}) \right\| _ {2} ^ {2}. \tag {6}
\]

We combine the two loss terms and use \(\lambda_{edge}\) as the balancing coefficient in the complete loss function for stage 2:

\[
\mathcal {L} = \mathcal {L} _ {i m g} + \lambda_ {e d g e} \mathcal {L} _ {e d g e}. \tag {7}
\]

The combination of glyph-aware ControlNet conditioning and edge-constrained training objectives enables our model to preserve stroke integrity while harmonizing text and background appearance.

## 4. Dataset and Benchmark

Existing datasets like Ma et al. [31] offer only subtle degradation, as shown in Fig. 3 (a), making them insufficient for evaluating model robustness. To address the lack of both challenging and publicly available datasets tailored for scene text image super-resolution, especially for Chinese text, we introduce UZ-ST, a challenging real-world benchmark. It is collected using ViVO X200 Ultra equipped with four fixed focal lengths (14 mm, 35 mm, 85 mm, 200 mm), enabling image pairs with a maximum zoom of ×14.29. It includes diverse scenes—street views, book covers, advertisements, menus, and posters—captured under varied lighting, with all text lines manually annotated. However, such zoom introduces severe misalignment that breaks pixel-wise optimization methods like [2], originally designed for moderate ×2 to ×4 zoom. To address this, we design a Cascade Coarse-to-fine Alignment pipeline (see Fig. 3 (b)): images are first sorted by focal length, and each low-quality image is sequentially aligned to its next higher-focal neighbor using optimization-based registration or feature-based extractors [22, 29], then refined against the 200 mm ground truth. Finally, we manually filter or realign problematic cases to ensure precise alignment.

Through meticulous annotation and alignment, we obtained 5,036 image pairs with 49,675 text lines. We treat images captured under 200 mm focal lengths as GT, yielding 1,439, 1,798, and 1,799 pairs for the ×14.29, ×5.71,

and ×2.35 zoom modes, respectively. Among them, we randomly select 470, 589, and 581 pairs for evaluation under each zoom mode. Each image pair contains one or more text lines. These evaluation sets allow us to assess model performance in more complex and challenging scenarios.

For the UZ-ST-benchmark, we utilize 5 evaluation metrics to examine the quality of image super-resolution on the scale of the full image. Firstly, we adopt Peak Signal-to-Noise Ratio (PSNR), Structural Similarity Index Measure (SSIM) [42], Learned Perceptual Image Patch Similarity (LPIPS) [57], Deep Image Structure and Texture Similarity (DISTS) [10], and Fréchet Inception Distance (FID) [17] for evaluation of image quality. Specifically, PSNR and SSIM are computed in the pixel space to quantify low-level reconstruction fidelity, LPIPS and DISTS are computed in the feature space to assess perceptual similarity, and FID is employed to evaluate the distributional discrepancy between generated and real images. However, these metrics do not directly reflect the quality or accuracy of super-resolved text. To address this, we crop annotated text regions from the images and compute PSNR, SSIM, LPIPS, and DISTS on these cropped regions, denoted as PSNRcr, SSIMcr, LPIPScr, and DISTScr. For text accuracy, we apply an OCR model to recognize the text and compare its outputs with the ground-truth annotations using the Levenshtein ratio [54]:

\[
\mathrm{OCR-A} = \frac {\operatorname{Len} \left(s _ {p r e d}\right) + \operatorname{Len} \left(s _ {g t}\right) - \operatorname{Dist} \left(s _ {p r e d} , s _ {g t}\right)}{\operatorname{Len} \left(s _ {p r e d}\right) + \operatorname{Len} \left(s _ {g t}\right)}, \tag {8}
\]

where  \( s_{pred} \)  stands for the predicted text sequence,  \( s_{gt} \)  denotes annotated ground-truth text sequence, and  \( \text{Dist}(\cdot,\cdot) \)  is the Levenshtein distance between text sequences.

## 5. Experiment

### 5.1. Implementation Details

We combine synthetic data (built upon LSDIR [26] with text rendered via LBTS [38] and Real-ESRGAN [44] degradation) and real data from Real-CE [31] and UZ-ST. Misaligned pairs in Real-CE are filtered and reannotated, yielding 337 training and 188 testing pairs. Stage 1 uses cropped text regions and is trained using an IDM-based architecture [58] with combined segmentation and reconstruction losses. Stage 2 is based on Stable Diffusion 3.5 [16] and employs a tile-based inference strategy [19, 50]; it is pretrained on synthetic data and fine-tuned on real data. For more details, see the Sec. 11.

### 5.2. Comparison Results

#### 5.2.1. Quantitative Results

We evaluate existing competing methods, including GAN-based image super-resolution approaches such as Real-ESRGAN [44] and HAT [5]; diffusion-based approaches

## B-ocr-94f15b7ac1c95e

B PDF page 10

Xiaoguang Hu, Dianhai Yu, and Yanjun Ma. Pp-ocrv3: More attempts for the improvement of ultra lightweight OCR system. CoRR, abs/2206.03001, 2022. 1

[24] Peidong Li and Dixiao Cui. Navigation-guided sparse scene representation for end-to-end autonomous driving. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025. 1

[25] Xiaoming Li, Wangmeng Zuo, and Chen Change Loy. Learning generative structure prior for blind text image super-resolution. In CVPR, pages 10103-10113, 2023. 1, 2, 3, 6

[26] Yawei Li, Kai Zhang, Jingyun Liang, Jiezhang Cao, Ce Liu, Rui Gong, Yulun Zhang, Hao Tang, Yun Liu, Denis Demandolx, et al. Lsdir: A large scale dataset for image restoration. In CVPRW, pages 1775–1787, 2023. 5, 1

[27] Xinqi Lin, Jingwen He, Ziyan Chen, Zhaoyang Lyu, Bo Dai, Fanghua Yu, Yu Qiao, Wanli Ouyang, and Chao Dong. Diffbir: Toward blind image restoration with generative diffusion prior. In ECCV, pages 430–448, 2024. 2, 6

[28] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101, 2017. 1

[29] David G Lowe. Object recognition from local scale-invariant features. In Proceedings of the seventh IEEE international conference on computer vision, pages 1150–1157. Ieee, 1999. 5

[30] Jianqi Ma, Zhetong Liang, and Lei Zhang. A text attention network for spatial deformation robust scene text image super-resolution. In CVPR, pages 5911-5920, 2022. 3

[31] Jianqi Ma, Zhetong Liang, Wangmeng Xiang, Xi Yang, and Lei Zhang. A benchmark for chinese-english scene text image super-resolution. In ICCV, pages 19452–19461, 2023. 2, 5, 6, 1

[32] Yongqiang Mou, Lei Tan, Hui Yang, Jingying Chen, Leyuan Liu, Rui Yan, and Yaohong Huang. Plugnet: Degradation aware scene text recognition supervised by a pluggable super-resolution unit. In ECCV, pages 158–174, 2020. 3

[33] Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:2204.06125, 2022. 1

[34] Richard A Roberts and Clifford T Mullis. Digital signal processing. Addison-Wesley Longman Publishing Co., Inc., 1987. 5

[35] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In CVPR, pages 10684-10695, 2022. 1, 3

[36] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L Denton, Kamyar Ghasemipour, Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, et al. Photorealistic text-to-image diffusion models with deep language understanding. Advances in neural information processing systems, 35:36479–36494, 2022. 1

[37] Mohamed Ali Souibgui, Sanket Biswas, Andres Mafla, Ali Furkan Biten, Alicia Fornés, Yousri Kessentini, Josep Lladós, Lluis Gomez, and Dimosthenis Karatzas. Text-diae:

a self-supervised degradation invariant autoencoder for text recognition and document enhancement. In proceedings of the AAAI conference on artificial intelligence, pages 2330-2338, 2023. 1

[38] Zhengmi Tang, Tomo Miyazaki, and Shinichiro Omachi. A scene-text synthesis engine achieved through learning from decomposed real-world data. IEEE Transactions on Image Processing, 32:5837–5851, 2023. 5, 1

[39] Yuxiang Tuo, Wangmeng Xiang, Jun-Yan He, Yifeng Geng, and Xuansong Xie. Anytext: Multilingual visual text generation and editing. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024. OpenReview.net, 2024. 1

[40] Bolin Wang, Xinyi Shen, and Kejun Zhang. Multi-task diffusion model for simultaneous text and image inpainting. In 2024 17th International Symposium on Computational Intelligence and Design (ISCID), pages 301–305. IEEE, 2024. 3

[41] Jianyi Wang, Zongsheng Yue, Shangchen Zhou, Kelvin CK Chan, and Chen Change Loy. Exploiting diffusion prior for real-world image super-resolution. IJCV, 132(12):5929-5949, 2024. 2

[42] Wenjia Wang, Enze Xie, Peize Sun, Wenhai Wang, Lixun Tian, Chunhua Shen, and Ping Luo. Textsr: Content-aware text super-resolution guided by recognition. arXiv preprint, 2019. 3, 5, 2

[43] Wenjia Wang, Enze Xie, Xuebo Liu, Wenhai Wang, Ding Liang, Chunhua Shen, and Xiang Bai. Scene text image super-resolution in the wild. In ECCV, pages 650–666, 2020. 2, 3

[44] Xintao Wang, Liangbin Xie, Chao Dong, and Ying Shan. Real-esrgan: Training real-world blind super-resolution with pure synthetic data. In ICCV, pages 1905–1914, 2021. 2, 5, 1

[45] Yufei Wang, Wenhan Yang, Xinyuan Chen, Yaohui Wang, Lanqing Guo, Lap-Pui Chau, Ziwei Liu, Yu Qiao, Alex C Kot, and Bihan Wen. Sinsr: diffusion-based image super-resolution in a single step. In CVPR, pages 25796–25805, 2024. 2

[46] Rongyuan Wu, Lingchen Sun, Zhiyuan Ma, and Lei Zhang. One-step effective diffusion network for real-world image super-resolution. NeurIPS, 37:92529–92553, 2024. 2, 6

[47] Rongyuan Wu, Tao Yang, Lingchen Sun, Zhengqiang Zhang, Shuai Li, and Lei Zhang. Seesr: Towards semantics-aware real-world image super-resolution. In CVPR, pages 25456-25467, 2024. 2, 6

[48] Tao Yang, Rongyuan Wu, Peiran Ren, Xuansong Xie, and Lei Zhang. Pixel-aware stable diffusion for realistic image super-resolution and personalized stylization. In ECCV, pages 74–91, 2024. 2

[49] Maoyuan Ye, Jing Zhang, Juhua Liu, Chenyu Liu, Baocai Yin, Cong Liu, Bo Du, and Dacheng Tao. Hi-sam: Marrying segment anything model for hierarchical text segmentation. TPAMI, 2024. 3, 4, 8, 1

[50] Fanghua Yu, Jinjin Gu, Zheyuan Li, Jinfan Hu, Xiangtao Kong, Xintao Wang, Jingwen He, Yu Qiao, and Chao Dong. Scaling up to excellence: Practicing model scaling for photorealistic image restoration in the wild. In CVPR, pages 25669–25680, 2024. 2, 5, 6, 1

## B-ocr-bd0bf36465dbe7

B PDF page 19

![img-17.jpeg](img-17.jpeg)

Figure 10. Detailed examples of UZ-ST.

## B-ocr-e0afad88a68cbc

B PDF page 2

Table 1. Dataset comparison. TextZoom [43] lacks Chinese, CTR [51] lacks multi-line text, and Real-CE [31] has mild degradation. UZ-ST covers all, enabling comprehensive evaluation.

[tbl-0.html](tbl-0.html)

(LR) inputs [13, 15, 19, 27, 46, 47, 50]. Although these approaches can effectively restore fine-grained natural textures (e.g., grass, leaves), they often distort text regions, turning them into gibberish as shown in Fig.1 (b). Because their primary goal is overall image enhancement, they tend to overlook text structure, resulting in a limited ability to preserve fine-grained glyph details. This limitation is amplified for Chinese characters, due to their complex and diverse glyph designs and relatively low saliency in images. Consequently, models tend to under-represent and collapse glyphs into oversimplified, averaged forms, producing overlapping or distorted characters. Some researchers attempt to address this by processing only text regions [25, 58]. While these methods improve readability notably, the absence of global background constraints often introduces style inconsistencies and block artifacts between text and background. Ultimately, current approaches face a persistent trade-off between maintaining readability and ensuring high image quality. Our key observation is that these goals need not be mutually exclusive if text and non-text are explicitly handled differently. Text structures can be reconstructed with dedicated mechanisms and then used to guide full-image restoration, ensuring coherent style without artifacts.

Building on this insight, we introduce TiGeSR (Text–Image Guided Super-Resolution), a progressive two-stage paradigm for scene text super-resolution built on the principle of “restoring text structure first, enhancing the whole image later.” Unlike methods that rely on a single generative prior, TiGeSR explicitly separates the treatment of text and non-text regions: a diffusion-based local text refiner focuses on reconstructing fine-grained stroke geometry in text regions, ensuring glyph fidelity and structural consistency. The recovered text structures are then injected as conditional guidance into the subsequent full-image restoration stage, steering global super-resolution to harmonize text and background while suppressing artifacts and preserving overall visual quality.

Moreover, existing scene text super-resolution datasets [31, 43, 51] are limited to mild degradation ( \( \leq \times 4 \) ), which fails to reflect real-world long-distance scenarios and restricts models from learning robust low-to high-resolution mappings. To address the issue of data scarcity and enable comprehensive evaluation [31, 43], we introduce the UZ-ST (UltraZoom-Sence Text) benchmark dataset, the first scene text dataset that contains a maximum

zooming mode of ×14.29, providing extra challenging scenarios for the field. Content differences are outlined in Tab. 1. It includes high-quality 5,036 LR-HR pairs captured at multiple focal lengths (ranging from 14mm to 200mm), with 49,675 text lines in total. Each pair comes with detailed annotations, including detection boxes and text transcripts, to support both training and evaluation. The dataset includes diverse scenarios such as shop signs, posters, and documents. It also covers varying lighting conditions, including daylight, indoor lighting, and nighttime, offering a challenging yet practical benchmark for the field. To ensure reliable alignment across focal lengths, we adopt a coarse-to-fine cascade alignment strategy combined with manual filtering: coarse alignment is performed via global geometric transformation, and residual misalignments are corrected through local refinement. This process achieves accurate LR-HR alignment, thereby ensuring both the quality of the dataset and the reliability of our experiments. The main contributions are summarized as follows:

1. We propose TiGeSR, the first two-stage scene text super-resolution framework with a 'text-first, image-later' paradigm that decouples glyph restoration from image enhancement, improving readability and visual quality.
2. We introduce UZ-ST, the first scene text benchmark with maximum zoom of \(\times 14.29\), offering aligned, richly annotated LR-HR pairs for thorough evaluation under challenging real-world conditions.
3. Extensive experiments on Real-CE and UZ-ST show our method outperforms prior state-of-the-art models, especially in preserving text structure.

## 2. Related Works

Real-World Image Super-Resolution. Real-world image super-resolution (Real-SR) aims to reconstruct high-resolution (HR) images from low-resolution (LR) inputs degraded under uncontrolled real-world conditions. Early GAN-based methods, such as BSRGAN [55] and Real-ESRGAN [44], synthesize degradations through random combinations of known distortions and use adversarial training for restoration. While they generate natural-looking images, their instability and insensitivity to fine details limit their ability to recover structural elements, especially text. Recent work introduces diffusion models into Real-SR [45, 53], improving perceptual quality but still struggling with complex structures like scene text. StableSR [41] and DiffBIR [27] apply ControlNet [56] to condition generation on LR inputs, while PASD [48] and SeeSR [47] incorporate high-level semantics to enhance fidelity. SUPIR [50] scales training with large image-text pairs and introduces degradation-robust encoders. Other approaches, including OSEDiff [46] and TSD-SR [14], directly apply the diffusion process on LR images and distill models for one-step sampling. DiT-SR [6], Dream

[OCR table id=tbl-0.html; page=2]
<table><tr><td>Content</td><td>TextZoom</td><td>CTR</td><td>Real-CE</td><td>UZ-ST (Ours)</td></tr><tr><td>Chinese characters</td><td>✕</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Multi-line text</td><td>✕</td><td>✕</td><td>√</td><td>√</td></tr><tr><td>Real-World Degradation(&gt;×4)</td><td>✕</td><td>✕</td><td>✕</td><td>√</td></tr></table>

## B-ocr-efa7a146fd40f0

B PDF page 12

# Restore Text First, Enhance Image Later: Two-Stage Scene Text Image Super-Resolution with Glyph Structure Guidance

Supplementary Material

## 7. Reproducibility Statement

To ensure reproducibility, we have made the following efforts:

1. We will release our code and dataset.
2. We provide implementation details in Sec. 5.1 and Sec. 11, including the training process and selection of hyper-parameters.
3. We provide details on evaluation metrics and dataset preparation in Sec. 4 and Sec. 10, and the code and data will be made available along with it.

## 8. Ethics Statement

This work focuses on improving scene text image super-resolution to support beneficial applications such as enhancing accessibility, document restoration, and navigation assistance. However, we acknowledge potential risks, including misuse in privacy-sensitive contexts (e.g., recovering text from personal or social media images) or unintended deployment in surveillance. To mitigate such risks, users are encouraged to combine our methods with privacy-preserving techniques such as watermarking or selective inpainting. Our UZ-ST dataset was collected from public, non-sensitive scenes under ethical guidelines, without including personally identifiable or private information. We believe the societal benefits of improved text image restoration outweigh potential risks, provided that the technology is applied responsibly.

## 9. LLM Acknowledgments

We thank ChatGPT (GPT-5) and DeepSeek for the help in refining the language and improving clarity. All wording and factual content were reviewed and approved by the authors.

## 10. Dataset Collection

We use VIVO X200 Ultra to collect images for 4 separate focal lengths (14 mm, 35 mm, 84 mm, and 200 mm). We first use PP-OCRV5 [7] for the rough annotation, then we manually filter the images and annotations. During the filtering and annotation, each image undergoes the following rules:

- Width or height of the image should be no less than 256.
- Height of the text should not be less than 32 pixels.
- Score of OCR recognition of the text should not be lower than 0.9.

- Content of the text should not be empty or consist solely of whitespace.

## 11. More Implementation Details

Dataset Settings. For training, we combine a synthetic dataset with real paired datasets (Real-CE [31] and UZ-ST). Our synthetic dataset builds upon LSDIR [26], containing 27,000 triplets ($x_H, x_L, x_m$). We render text on the GT of LSDIR and the corresponding text mask using the LBTS [38], then apply Real-ESRGAN degradation Wang et al. [44] to generate LR images. Since there are misaligned image pairs in Real-CE [19, 58] and text lines not annotated, we filter out misaligned image pairs and reannotate the images manually. In the end, we obtain 337 training pairs and 188 testing pairs from the Real-CE dataset. Images under 13mm and 52mm focal lengths are considered as LR $x_L$ and GT $x_H$, respectively. Following Hu et al. [19], we use SAM-TS [49] to obtain the text mask $x_m$ from $x_H$. UZ-ST triplets ($x_H, x_L, x_m$) are processed identically. For stage 1 training, we use cropped text regions from the dataset, while for stage 2, we use full images. Following [39], we use PP-OCRv3 [23] to extract strings from the text region of predicted SR for evaluation of OCR-A.

Training Details. For stage 1, we build our model based on the IDM baseline of DiffTSR [58]. We set $\lambda_{td}$, $\lambda_{Seg}$, $\lambda_{Focal}$, and $\lambda_{Dice}$ as 1, 0.1, 20, and 1 respectively. In stage 2, our model is built upon Stable Diffusion 3.5 medium [16] and follows a similar tile-based inference strategy to TADiSR [19] and SUPIR [50]. The timestep $t$ is set to 150. The conditioning scale of the ControlNet is set to 1.0. $\lambda_{t2}$, $\lambda_{LPIPS}$, and $\lambda_{edge}$ are set to 1, 5, 100 when using the synthetic dataset for pretraining. Then, $\lambda_{edge}$ is set to 0 and the remaining coefficients are kept unchanged when training on real paired datasets. We train both stages of the model using the AdamW [28] optimizer and set the learning rate to $5 \times 10^{-5}$ and $5 \times 10^{-6}$ for stages 1 and 2 separately. All experiments are conducted on NVIDIA H20 GPUs. For stage 1, we train the model on synthetic and real datasets for 8 epochs, then finetune it on synthetic data for 2 epochs. For stage 2, we first pretrain the model on the synthetic dataset for 50 epochs. Then we train on the real paired datasets for 50 epochs.

## 12. More details of UZ-ST

In Tab. 7, we provide detailed statistics on the composition of the UZ-ST dataset. Additionally, in Fig. 10, we present
