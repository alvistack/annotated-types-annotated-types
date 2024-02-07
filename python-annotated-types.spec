# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-annotated-types
Epoch: 100
Version: 0.6.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Reusable constraint types to use with typing.Annotated
License: MIT
URL: https://github.com/annotated-types/annotated-types/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package provides metadata objects which can be used to represent
common constraints such as upper and lower bounds on scalar values and
collection sizes, a Predicate marker for runtime checks, and
descriptions of how we intend these metadata to be interpreted. In some
cases, we also note alternative representations which do not require
this package.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-annotated-types
Summary: Reusable constraint types to use with typing.Annotated
Requires: python3
Requires: python3-typing-extensions >= 4.0.0
Provides: python3-annotated-types = %{epoch}:%{version}-%{release}
Provides: python3dist(annotated-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-annotated-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(annotated-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-annotated-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(annotated-types) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-annotated-types
This package provides metadata objects which can be used to represent
common constraints such as upper and lower bounds on scalar values and
collection sizes, a Predicate marker for runtime checks, and
descriptions of how we intend these metadata to be interpreted. In some
cases, we also note alternative representations which do not require
this package.

%files -n python%{python3_version_nodots}-annotated-types
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-annotated-types
Summary: Reusable constraint types to use with typing.Annotated
Requires: python3
Requires: python3-typing-extensions >= 4.0.0
Provides: python3-annotated-types = %{epoch}:%{version}-%{release}
Provides: python3dist(annotated-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-annotated-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(annotated-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-annotated-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(annotated-types) = %{epoch}:%{version}-%{release}

%description -n python3-annotated-types
This package provides metadata objects which can be used to represent
common constraints such as upper and lower bounds on scalar values and
collection sizes, a Predicate marker for runtime checks, and
descriptions of how we intend these metadata to be interpreted. In some
cases, we also note alternative representations which do not require
this package.

%files -n python3-annotated-types
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-annotated-types
Summary: Reusable constraint types to use with typing.Annotated
Requires: python3
Requires: python3-typing-extensions >= 4.0.0
Provides: python3-annotated-types = %{epoch}:%{version}-%{release}
Provides: python3dist(annotated-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-annotated-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(annotated-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-annotated-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(annotated-types) = %{epoch}:%{version}-%{release}

%description -n python3-annotated-types
This package provides metadata objects which can be used to represent
common constraints such as upper and lower bounds on scalar values and
collection sizes, a Predicate marker for runtime checks, and
descriptions of how we intend these metadata to be interpreted. In some
cases, we also note alternative representations which do not require
this package.

%files -n python3-annotated-types
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
