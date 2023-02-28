# reporter
This tool can help u for writing pentest report. For example, u have 100 PoCs of same vuln for different host. 

## Installation
```
git clone https://github.com/stderr2d0ma1n/reporter
pip3 install docxtpl
```
## Usage
[!] Screenshots in directory must be in format: 10_1_2_3.jpg or 192_168_0_1.png
```
python3 reporter.py -t template.docx -d dir_with_pocs -o output.docx
```
## Example of template
![изображение](https://user-images.githubusercontent.com/113356347/221852845-3ba1508e-e196-4d97-a714-e726dfef6ca7.png)
