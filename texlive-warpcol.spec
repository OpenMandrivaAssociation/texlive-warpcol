Name:		texlive-warpcol
Version:	15878
Release:	2
Summary:	Relative alignment of rows in numeric columns in tabulars
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/warpcol
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/warpcol.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/warpcol.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/warpcol.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines a tabular column type for formatting numerical columns
in LaTeX. The column type enables numerical items to be right
justified relative to each other, while centred beneath the
column label. In addition, macros are provided to enable
variations on this column type to be defined. Usage of the
package is superficially similar to that of dcolumn; however,
the alignment scheme is different, and the packages have
different, though overlapping, applications.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/warpcol/warpcol.sty
%doc %{_texmfdistdir}/doc/latex/warpcol/README
%doc %{_texmfdistdir}/doc/latex/warpcol/warpcol.pdf
#- source
%doc %{_texmfdistdir}/source/latex/warpcol/warpcol.dtx
%doc %{_texmfdistdir}/source/latex/warpcol/warpcol.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
