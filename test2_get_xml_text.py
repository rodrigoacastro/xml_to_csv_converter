from bs4 import BeautifulSoup as parser

def parse_xml (xml_file: str):
    output = parser(xml_file, features='xml')
    return (output)


# link: https://stackoverflow.com/questions/11351183/how-to-get-xml-tag-value-in-python

xml_sample2 = """
<?xml version="1.0" encoding="utf-8"?>
<LogFile xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <VersionString>2.0.1.222</VersionString>
  <Subject>FBS105_T1_EL1</Subject>
  <startTime>2022-08-31T13:52:11.8241334-03:00</startTime>
  <endTime>2022-08-31T14:02:35.0951334-03:00</endTime>
  <Project>
    <FileName>C:\Users\Letra\Desktop\CROSS\Projetos das Atividades\T1_EL1.project</FileName>
    <Description>example project description</Description>
    <versionString />
    <useSourceText>true</useSourceText>
    <promptSubjectName>true</promptSubjectName>
    <useExtendedTranslations>false</useExtendedTranslations>
    <showTimer>false</showTimer>
    <maxWindow>false</maxWindow>
    <offlineGWM>false</offlineGWM>
    <fullScreen>false</fullScreen>
    <lockWindows>false</lockWindows>
	<Languages source="pt" target="pt" task="revision"/> 
    <Plugins>
      <EyeSampler />
      <Key_Logger />
    </Plugins>
    <Interface>
      <Standard>
        <pluginDependances />
        <Settings>
          <TargetBackgroundColor RGB="-1" />
          <SourceBackgroundColor RGB="-1" />
          <lineHeight source="1" target="1" />
          <SourceText>{\rtf1\ansi\ansicpg1252\deff0\deflang1046{\fonttbl{\f0\fnil\fcharset0 Microsoft Sans Serif;}{\f1\fswiss\fprq2\fcharset0 Arial;}}
\viewkind4\uc1\pard\sl180\slmult1\f0\fs32\par
\lang1033\f1 Idioma: portugu\'eas. Par\'e1grafo \'fanico, m\'ednimo de 100 (aprox. 6 linhas) e m\'e1ximo de 250 palavras (aprox. 13 linhas). N\'e3o colocar t\'edtulo, refer\'eancias/cita\'e7\'f5es ou palavras-chave. Incluir objetivos, m\'e9todos, resultados (preliminares) e poss\'edveis contribui\'e7\'f5es.\b\par
}
</SourceText>
          <TargetText>{\rtf1\ansi\ansicpg1252\deff0\deflang1046{\fonttbl{\f0\fnil\fcharset0 Microsoft Sans Serif;}}
\viewkind4\uc1\pard\sl180\slmult1\f0\fs32\par
}
</TargetText>
          <SourceTextUTF8>
Idioma: português. Parágrafo único, mínimo de 100 (aprox. 6 linhas) e máximo de 250 palavras (aprox. 13 linhas). Não colocar título, referências/citações ou palavras-chave. Incluir objetivos, métodos, resultados (preliminares) e possíveis contribuições.</SourceTextUTF8>
          <TargetTextUTF8 />
          <TranslationWindow X="0" Y="10" Width="1296" Height="950" Split="92" STO="True" VHO="Horizontal" />
        </Settings>
        <SourceField X="5" Y="27" Width="1264" Height="490" />
        <TargetField X="5" Y="27" Width="1264" Height="492" />
        <Import2006Flag>false</Import2006Flag>
      </Standard>
    </Interface>
  </Project>
  </FinalTextChar>
</LogFile>  
"""

# from bs4 import BeautifulSoup as parse_xml

soup2 = parse_xml(xml_sample2)
print(soup2.find('Project'))


