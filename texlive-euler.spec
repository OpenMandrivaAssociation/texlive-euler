Name:		texlive-euler
Version:	42428
Release:	2
Summary:	Use AMS Euler fonts for math
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/euler
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euler.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euler.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euler.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a setup for using the AMS Euler family of fonts for
mathematics in LaTeX documents. "The underlying philosophy of
Zapf's Euler design was to capture the flavour of mathematics
as it might be written by a mathematician with excellent
handwriting." [concrete-tug] The euler package is based on
Knuth's macros for the book 'Concrete Mathematics'. The text
fonts for the Concrete book are supported by the beton package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/euler/euler.sty
%doc %{_texmfdistdir}/doc/latex/euler/euler.pdf
%doc %{_texmfdistdir}/doc/latex/euler/legal.txt
#- source
%doc %{_texmfdistdir}/source/latex/euler/euler.dtx
%doc %{_texmfdistdir}/source/latex/euler/euler.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
