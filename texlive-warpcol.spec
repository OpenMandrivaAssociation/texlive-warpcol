%global tl_name warpcol
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0c
Release:	%{tl_revision}.1
Summary:	Relative alignment of rows in numeric columns in tabulars
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/warpcol
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/warpcol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/warpcol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/warpcol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines a tabular column type for formatting numerical columns in LaTeX.
The column type enables numerical items to be right justified relative
to each other, while centred beneath the column label. In addition,
macros are provided to enable variations on this column type to be
defined. Usage of the package is superficially similar to that of
dcolumn; however, the alignment scheme is different, and the packages
have different, though overlapping, applications.

