# revision 30105
# category Package
# catalog-ctan /language/japanese/zxjafont
# catalog-date 2013-04-25 17:40:06 +0200
# catalog-license other-free
# catalog-version 0.2
Name:		texlive-zxjafont
Version:	0.2
Release:	2
Summary:	Set up Japanese font families for XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/zxjafont
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zxjafont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zxjafont.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive zxjafont package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/zxjafont/zxjafont.sty
%doc %{_texmfdistdir}/doc/latex/zxjafont/LICENSE
%doc %{_texmfdistdir}/doc/latex/zxjafont/README
%doc %{_texmfdistdir}/doc/latex/zxjafont/zxjafont.pdf
%doc %{_texmfdistdir}/doc/latex/zxjafont/zxjafont.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
