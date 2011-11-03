# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/warpcol
# catalog-date 2007-11-21 20:02:33 +0100
# catalog-license lppl
# catalog-version 1.0c
Name:		texlive-warpcol
Version:	1.0c
Release:	1
Summary:	Relative alignment of rows in numeric columns in tabulars
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/warpcol
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/warpcol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/warpcol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/warpcol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Defines a tabular column type for formatting numerical columns
in LaTeX. The column type enables numerical items to be right
justified relative to each other, while centred beneath the
column label. In addition, macros are provided to enable
variations on this column type to be defined. Usage of the
package is superficially similar to that of dcolumn; however,
the alignment scheme is different, and the packages have
different, though overlapping, applications.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/warpcol/warpcol.sty
%doc %{_texmfdistdir}/doc/latex/warpcol/README
%doc %{_texmfdistdir}/doc/latex/warpcol/warpcol.pdf
#- source
%doc %{_texmfdistdir}/source/latex/warpcol/warpcol.dtx
%doc %{_texmfdistdir}/source/latex/warpcol/warpcol.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}