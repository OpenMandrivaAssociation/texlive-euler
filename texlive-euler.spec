%global tl_name euler
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5
Release:	%{tl_revision}.1
Summary:	Use AMS Euler fonts for math
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/euler
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euler.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euler.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euler.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides a setup for using the AMS Euler family of fonts for mathematics
in LaTeX documents. "The underlying philosophy of Zapf's Euler design
was to capture the flavour of mathematics as it might be written by a
mathematician with excellent handwriting." The euler package is based on
Knuth's macros for the book 'Concrete Mathematics'. The text fonts for
the Concrete book are supported by the beton package.

