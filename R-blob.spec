#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-blob
Version  : 1.2.3
Release  : 48
URL      : https://cran.r-project.org/src/contrib/blob_1.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/blob_1.2.3.tar.gz
Summary  : A Simple S3 Class for Representing Vectors of Binary Data
Group    : Development/Tools
License  : MIT
Requires: R-rlang
Requires: R-vctrs
BuildRequires : R-rlang
BuildRequires : R-vctrs
BuildRequires : buildreq-R

%description
What if you want to put a vector of them in a data frame? The 'blob'
    package provides the blob object, a list of raw vectors, suitable for
    use as a column in data frame.

%prep
%setup -q -c -n blob
cd %{_builddir}/blob

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649604864

%install
export SOURCE_DATE_EPOCH=1649604864
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library blob
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library blob
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library blob
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc blob || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/blob/DESCRIPTION
/usr/lib64/R/library/blob/INDEX
/usr/lib64/R/library/blob/LICENSE
/usr/lib64/R/library/blob/Meta/Rd.rds
/usr/lib64/R/library/blob/Meta/features.rds
/usr/lib64/R/library/blob/Meta/hsearch.rds
/usr/lib64/R/library/blob/Meta/links.rds
/usr/lib64/R/library/blob/Meta/nsInfo.rds
/usr/lib64/R/library/blob/Meta/package.rds
/usr/lib64/R/library/blob/NAMESPACE
/usr/lib64/R/library/blob/NEWS.md
/usr/lib64/R/library/blob/R/blob
/usr/lib64/R/library/blob/R/blob.rdb
/usr/lib64/R/library/blob/R/blob.rdx
/usr/lib64/R/library/blob/help/AnIndex
/usr/lib64/R/library/blob/help/aliases.rds
/usr/lib64/R/library/blob/help/blob.rdb
/usr/lib64/R/library/blob/help/blob.rdx
/usr/lib64/R/library/blob/help/paths.rds
/usr/lib64/R/library/blob/html/00Index.html
/usr/lib64/R/library/blob/html/R.css
/usr/lib64/R/library/blob/tests/testthat.R
/usr/lib64/R/library/blob/tests/testthat/blob.txt
/usr/lib64/R/library/blob/tests/testthat/helper-deprecate.R
/usr/lib64/R/library/blob/tests/testthat/test-accessors.R
/usr/lib64/R/library/blob/tests/testthat/test-cast.R
/usr/lib64/R/library/blob/tests/testthat/test-construction.R
/usr/lib64/R/library/blob/tests/testthat/test-format.R
/usr/lib64/R/library/blob/tests/testthat/test-missing.R
