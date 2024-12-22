from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from typing import Any, NamedTuple, Optional, TypedDict, Literal
from types import SimpleNamespace
from conans.model.options import Options

type Nation = Literal["asia", "america"]


class Address(NamedTuple):
    region: Nation
    street: Optional[str] = None


option = Address(region="america")


class ConanOptions(NamedTuple):
    shared: bool
    fPIC: bool


type HellOption = Literal["arch", "build_type", "compiler", "os"]
type OptionList = list[HellOption]


class ConanSetting(NamedTuple):
    os: Optional[str] = None
    compiler: Optional[str] = None
    build_type: Optional[str] = None
    arch: Optional[str] = None


type ConanSettingType = tuple[str]

type BooleanTuple = tuple[bool, bool]
type OptionType = dict[str, BooleanTuple]

op: OptionType = {"shared": (True, False)}


class helloRecipe(ConanFile):
    name = "hello"
    version = "0.1"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of hello package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = ["arch", "build_type", "compiler", "os"]
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":  # type: ignore
            self.options.rm_safe("fPIC")  # type: ignore

    def configure(self):
        if self.options.shared:  # type: ignore
            self.options.rm_safe("fPIC")  # type: ignore

    def layout(self):
        self.folders.source
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["hello"]
