# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named KaleidoscopeExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from KaleidoscopeExt import *
except ImportError:
    pass

def getPluginID():
    return "kaleidoscope"

def getLabel():
    return "Kaleidoscope"

def getVersion():
    return 1

def getIconPath():
    return "kaleidoscope.png"

def getGrouping():
    return "Community/Filter"

def getPluginDescription():
    return "Creates kaleidoscope effects"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)

    # Create the user parameters
    lastNode.param = lastNode.createPageParam("param", "Parameter")
    param = lastNode.createChoiceParam("KL_type", "Type")
    entries = [ ("Type 1", ""),
    ("Type 2", ""),
    ("Type 3", ""),
    ("Type 4", ""),
    ("Type 5", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.param.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.KL_type = param
    del param

    param = lastNode.createDoubleParam("Shadertoy2paramValueFloat1", "Fractal Scale")
    param.setMinimum(0, 0)
    param.setMaximum(10, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(10, 0)
    param.setDefaultValue(10, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.param.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueFloat1 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy2paramValueFloat2", "Size")
    param.setMinimum(0.09999999999999999, 0)
    param.setMaximum(10, 0)
    param.setDisplayMinimum(0.09999999999999999, 0)
    param.setDisplayMaximum(10, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.param.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueFloat2 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy2paramValueFloat3", "Distort X")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)

    # Add the param to the page
    lastNode.param.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueFloat3 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy2paramValueFloat4", "Distort Y")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)

    # Add the param to the page
    lastNode.param.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueFloat4 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy2paramValueFloat5", "Rotation")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)

    # Add the param to the page
    lastNode.param.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueFloat5 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy2paramValueFloat6", "Mirror Multiplyer")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)

    # Add the param to the page
    lastNode.param.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueFloat6 = param
    del param

    lastNode.credit = lastNode.createPageParam("credit", "credit")
    param = lastNode.createSeparatorParam("sp", "Implemented by CGVIRUS")

    # Add the param to the page
    lastNode.credit.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sp = param
    del param

    param = lastNode.createSeparatorParam("sp2", "")

    # Add the param to the page
    lastNode.credit.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sp2 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['param', 'Settings', 'credit', 'Node'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Shadertoy2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy2")
    lastNode.setLabel("Shadertoy2")
    lastNode.setPosition(937, 304)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy2 = lastNode

    param = lastNode.getParam("paramValueInt0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramValueFloat2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueFloat3")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueFloat4")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueFloat5")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueFloat6")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("imageShaderFileName")
    if param is not None:
        param.setValue("/home/production/Desktop/keli.frag")
        del param

    param = lastNode.getParam("imageShaderPreset")
    if param is not None:
        param.set("Effect/Kaleidoscope")
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("/***  \n    Port of https://www.shadertoy.com/view/XsfGzj\n    Implementation and Enhancement by CGVIRUS for Natron Community\n***/\n\n// iChannel0: Source, filter=linear, wrap=clamp\n// BBox: iChannel0\n\n\nuniform int mode = 0; // Type, min=0, max=4\nuniform float amount = 10.0; // Fractal Scale, min=0.0, max=10.0\nuniform float size = 1.0; // Size, min=.1, max=10.0\nuniform float distortX = 0.0; // Distort X, min=0.0\nuniform float distortY = 0.0; // Distort Y, min=0.0\nuniform float rot = 0.0; // Rotation, min=0.0\nuniform float parallax = 0.0; // Mirror Multiplyer, min=0.0\nvec2 mirror(vec2 x)\n{\n        return abs(fract(x/2.0) - 0.5)*2.0;\n}\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n        vec2 uv = ((2*fragCoord.xy - iResolution.xy)/iResolution.x)/size;\n\n        float a = (parallax)*.001;\n        vec4 color = vec4(0.0);\n        \n        float rot = radians(rot);\n        mat2 m = mat2(cos(rot), -sin(rot), sin(rot), cos(rot));\n   \t\n\n        for (float i = 1.0; i < 10.0; i += 1.0) {\n                uv = vec2(sin(a)*uv.y - cos(a)*uv.x, sin(a)*uv.x + cos(a)*uv.y);\n                uv = mirror(uv*(amount*0.1));\n                uv  = m*uv;\n\n                if(mode == 0)\n                {a += i+distortX;\n                a /= i+distortY;}\n\n                else if(mode == 1)\n                {a *= i+distortX;\n                a -= i+distortY;}\n                \n                else if(mode == 2)\n                {a -= i+distortX;\n                a *= i+distortY;}\n                \n                else if(mode == 3)\n                {a /= i+distortX;\n                a += i+distortY;}\n                \n                else if(mode == 4)\n                {a += i+distortX;\n                a -= i+distortY;}\n                \n                else if(mode == 5)\n                {a -= i+distortX;\n                a += i+distortY;}     \n        }\n\n        fragColor = texture2D(iChannel0, mirror(uv*vec2(1.,iResolution.x/iResolution.y)*2.0));\n}")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap0")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(7, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("mode")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Type")
        del param

    param = lastNode.getParam("paramMinInt0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxInt0")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("amount")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Fractal Scale")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("size")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Size")
        del param

    param = lastNode.getParam("paramDefaultFloat2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat2")
    if param is not None:
        param.setValue(0.09999999999999999, 0)
        del param

    param = lastNode.getParam("paramMaxFloat2")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("distortX")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Distort X")
        del param

    param = lastNode.getParam("paramMinFloat3")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("distortY")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("Distort Y")
        del param

    param = lastNode.getParam("paramMinFloat4")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("rot")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("Rotation")
        del param

    param = lastNode.getParam("paramMinFloat5")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("parallax")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("Mirror Multiplyer")
        del param

    param = lastNode.getParam("paramMinFloat6")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Shadertoy2"

    # Start of node "Input1"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input1")
    lastNode.setLabel("Shadertoy2_Source")
    lastNode.setPosition(469, 156)
    lastNode.setSize(104, 31)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput1 = lastNode

    del lastNode
    # End of node "Input1"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(937, 425)
    lastNode.setSize(104, 31)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupShadertoy2.connectInput(0, groupInput1)
    groupOutput1.connectInput(0, groupShadertoy2)

    param = groupShadertoy2.getParam("paramValueInt0")
    param.setExpression("thisGroup.KL_type.get()", False, 0)
    del param
    param = groupShadertoy2.getParam("paramValueFloat1")
    group.getParam("Shadertoy2paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueFloat2")
    group.getParam("Shadertoy2paramValueFloat2").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueFloat3")
    group.getParam("Shadertoy2paramValueFloat3").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueFloat4")
    group.getParam("Shadertoy2paramValueFloat4").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueFloat5")
    group.getParam("Shadertoy2paramValueFloat5").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueFloat6")
    group.getParam("Shadertoy2paramValueFloat6").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["KaleidoscopeExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)