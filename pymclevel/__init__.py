# Versioned data relative objects
MCEDIT_DEFS = {}
MCEDIT_IDS = {}  # Maps the numeric and name ids to entries in MCEDIT_DEFS

from directories import minecraftSaveFileDir
from . import items
from . import pocket
from .box import BoundingBox, FloatBox
from .entity import Entity, TileEntity
from .faces import faceDirections, FaceXDecreasing, FaceXIncreasing, FaceYDecreasing, FaceYIncreasing, FaceZDecreasing, \
    FaceZIncreasing, MaxDirections
from .indev import MCIndevLevel
from .infiniteworld import ChunkedLevelMixin, AnvilChunk, MCAlphaDimension, MCInfdevOldLevel, ZeroChunk
from .javalevel import MCJavaLevel
from .level import ChunkBase, computeChunkHeightMap, EntityLevel, FakeChunk, LightedChunk, MCLevel
from .leveldbpocket import PocketLeveldbWorld
from .materials import alphaMaterials, classicMaterials, indevMaterials, MCMaterials, namedMaterials, pocketMaterials
from .mclevel import fromFile, loadWorld, loadWorldNumber
from .mclevelbase import ChunkNotPresent, PlayerNotFound
from .nbt import load, gunzip, TAG_Byte, TAG_Byte_Array, TAG_Compound, TAG_Double, TAG_Float, TAG_Int, TAG_Int_Array, \
    TAG_List, TAG_Long, TAG_Short, TAG_String
from .schematic import INVEditChest, MCSchematic, ZipSchematic

saveFileDir = minecraftSaveFileDir
