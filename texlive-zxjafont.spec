%global tl_name zxjafont
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Set up Japanese font families for XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/zxjafont
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zxjafont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zxjafont.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Set up Japanese font families for XeLaTeX

